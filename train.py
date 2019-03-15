"""
Filename: train.py
Created on Wed Mar 13 13:40:25 CST 2019

@author: Kefeng Zhu (zkf1985@gmail.com, zkf85@163.com)

== Plant Disease Recognition (PDR) ==
Train Models Main Script

"""
import os
import json
import time

from tensorflow.keras import optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, TensorBoard, ReduceLROnPlateau, CSVLogger

import config
from utils import print_title, plot_loss_acc, plot_lr
from model import build_model

def main():

    print_title('[PDR] Train Model', symbol='*')
    print_title('@author: Kefeng Zhu (zkf1985@gmail.com, zkf85@163.com)', '')
    print_title('Date: %s' % config.date, '')

    # 1. Make dirs/Show parameters
    if not os.path.exists(config.model_save_dir):
        os.mkdir(config.model_save_dir)
    # Print and save parameteres
    print_title('I. Training Parameters')
    config.print_params()

    # 2. Build and compile model
    print_title("II. Build Model")
    print('[KF INFO] Start building model ...')
    model = build_model(config.model_name, config.img_size, config.num_classes)
    optimizer = optimizers.Adam(lr=config.lr)
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    print('[KF INFO] Building model complete!')

    # 3. Callbacks
    callbacks = []
    callbacks.append(CSVLogger(os.path.join(config.model_save_dir, 'train_history.csv'), append=True, separator=';'))
    callbacks.append(ModelCheckpoint(os.path.join(config.model_save_dir, config.model_filename), monitor='val_loss', verbose=1, save_best_only=True, mode='auto'))
    if config.early_stopping_patience:
        callbacks.append(EarlyStopping(monitor='val_loss', patience=config.early_stopping_patience, verbose=1, mode='auto'))
    if config.lr_reduce_patience:
        callbacks.append(ReduceLROnPlateau(monitor='val_loss', factor=0.5, verbose=1, patience=config.lr_reduce_patience))

    # 4. Data generators
    print_title('III. Data Generator')
    print('[KF INFO] Initializing data generator ...')
    train_gen = ImageDataGenerator(
            rescale=1./255, rotation_range=24,
            width_shift_range=0.1, height_shift_range=0.1,
            shear_range=0.2, zoom_range=0.2,
            horizontal_flip=True, vertical_flip=True, fill_mode='nearest')
    train_flow = train_gen.flow_from_directory(
            config.train_data_dir,
            target_size=(config.img_size, config.img_size),
            batch_size=config.batch_size,
            class_mode='categorical')
    print('[KF INFO] training data flow from %s' % config.train_data_dir)
    val_gen = ImageDataGenerator(rescale=1./255)
    val_flow = val_gen.flow_from_directory(
            config.val_data_dir,
            target_size=(config.img_size, config.img_size),
            batch_size=config.batch_size,
            class_mode='categorical')
    print('[KF INFO] validation data flow from %s' % config.val_data_dir)
    # Save class indices
    with open(os.path.join(config.model_save_dir, config.class_indices_filename), 'w') as f:
        json.dump(train_flow.class_indices, f, indent=4)
        print('class_indices is saved to file: %s' % config.class_indices_filename)
    print('[KF INFO] Initializing data generator complete!')

    # 5. Train
    print_title('IV. Train Model')
    print('[KF INFO] Start Training ...')
    start = time.time()
    H = model.fit_generator(
            train_flow,
            validation_data=val_flow,
            epochs=config.epochs,
            steps_per_epoch=config.train_size // config.batch_size,
            validation_steps=config.val_size // config.batch_size,
            callbacks=callbacks)
    # Save training time:
    end = time.time()
    print('[KF INFO] Total training time :', end - start)
    print('[KF INFO] Training complete!')

    # 6. Save metric and plot
    print_title('V. Save Results')
    print('[KF INFO] Start saving results ...')
    # [Pitfall] Force casting float to all elements in the dictionary, 
    #  to prevent the "np.float32 cannot be Jsonity" problem.
    for k in H.history.keys():
        for i in range(len(H.history[k])):
            H.history[k][i] = float(H.history[k][i])
    # save
    with open(os.path.join(config.model_save_dir, config.history_filename), 'w') as f:
        json.dump(H.history, f, indent=4)
        print('[KF INFO] History is saved as "%s"' % config.history_filename)
    # load
    with open(os.path.join(config.model_save_dir, config.history_filename), 'r') as f:
        h = json.load(f)
    plot_loss_acc(h, config.model_save_dir, filename=config.plt_acc_loss_filename, title=config.prefix)
    if h.get('lr'):
        plot_lr(h, config.model_save_dir, filename=config.plt_lr_filename, title=config.prefix)
    print('[KF INFO] Saving results complete!') 


if __name__ == "__main__":
    main()
