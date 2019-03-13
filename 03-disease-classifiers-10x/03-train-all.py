"""
Filename: 03-train-all.py
Created on Wed Mar 13 13:40:25 CST 2019

@author: Kefeng Zhu (zkf1985@gmail.com, zkf85@163.com)

Description:
  Train specific disease recognition model
  Arguments:
    category_name: e.g. "apple"

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


#===============================================================================
# Main
#===============================================================================
def main():

    # 1. Make dirs/Show parameters
    # Create directory if needed
    if not os.path.exists(config.model_save_dir):
        os.mkdir(config.model_save_dir)

    config.print_params()
    config.save_params_to_log()

    # 2. Build and compile model
    print_title("Build Model")
    model = build_model(config.model_name, config.img_size, config.num_classes)
    optimizer = optimizers.Adam(lr=config.lr)
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()

    # 3. Callbacks
    callbacks = []
    callbacks.append(CSVLogger(os.path.join(config.model_save_dir, 'log.csv'), append=True, separator=';'))
    callbacks.append(ModelCheckpoint(os.path.join(config.model_save_dir, 'best_model.hdf5'), monitor='val_loss', verbose=1, save_best_only=True, mode='auto'))
    if config.early_stopping_patience:
        callbacks.append(EarlyStopping(monitor='val_loss', patience=config.early_stopping_patience, verbose=1, mode='auto'))
    if config.lr_reduce_patience:
        callbacks.append(ReduceLROnPlateau(monitor='val_loss', factor=0.5, verbose=1, patience=config.lr_reduce_patience))

    # 4. Data generators
    train_gen = ImageDataGenerator(
            rescale=1./255, rotation_range=24,
            width_shift_range=0.1, height_shift_range=0.1,
            shear_range=0.2, zoom_range=0.2,
            horizontal_flip=True, vertical_flip=True, fill_mode='nearest')
    train_flow = train_gen.flow_from_directory(
            config.train_data,
            target_size=(config.img_size, config.img_size),
            batch_size=config.batch_size,
            class_mode='categorical')
    val_gen = ImageDataGenerator(rescale=1./255)
    val_flow = val_gen.flow_from_directory(
            config.val_data,
            target_size=(config.img_size, config.img_size),
            batch_size=config.batch_size,
            class_mode='categorical')
    # Save class indices
    with open(os.path.join(config.model_save_dir, '%s_class_indices.json' % config.category_name), 'w') as f:
        json.dump(train_flow.class_indices, f, indent=4)
        print('class_indices is saved:', train_flow.class_indices)

    # 5. Train
    print_title('[KF INFO] Start Training ...')
    start = time.time()
    H = model.fit_generator(
            train_flow,
            validation_data=val_flow,
            epochs=config.epochs,
            steps_per_epoch=config.train_size // config.batch_size,
            validation_steps=config.val_size // config.batch_size,
            #epochs=2,                  # for testing
            #steps_per_epoch=10,        # for testing
            #validation_steps=10,       # for testing
            callbacks=callbacks)
    # Save training time:
    with open(os.path.join(config.model_save_dir, config.logfile), 'a') as f:
        print_title('Training Time', f=f)
        print(time.time() - start, file=f)

    print_title('[KF INFO] Training Completed!')

    # 6. Save metric and plot
    # Force casting float to all elements in the dictionary, 
    # to prevent the "np.float32 cannot be Jsonity" problem.
    for k in H.history.keys():
        for i in range(len(H.history[k])):
            H.history[k][i] = float(H.history[k][i])
    # save
    with open(os.path.join(config.model_save_dir, 'history.json'), 'w') as f:
        json.dump(H.history, f, indent=4)
        print("History is saved as 'history.json'")
    # load
    with open(os.path.join(config.model_save_dir, 'history.json'), 'r') as f:
        h = json.load(f)
    plot_loss_acc(h, config.model_save_dir, plt_name='%d%02d%02d-plt-acc-loss'%(config.now.year, config.now.month, config.now.day))
    if h.get('lr'):
        plot_lr(h, config.model_save_dir, plt_name='%d%02d%02d-plt-lr'%(config.now.year, config.now.month, config.now.day))


if __name__ == "__main__":
    main()
    #config.print_params()

