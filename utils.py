"""
Filename: utils.py 
Created on Wed Mar 13 13:40:25 CST 2019

@author: Kefeng Zhu (zkf1985@gmail.com, zkf85@163.com)

== Plant Disease Recognition (PDR) ==
Utility functions

"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


# Added on 2019/03/11
category_zh_dict = {
   'apple': '苹果',
   'cherry': '樱桃',
   'citrus': '桔子',
   'corn': '玉米',
   'grape': '葡萄',
   'peach': '桃子',
   'pepper': '辣椒',
   'potato': '土豆',
   'strawberry': '草莓',
   'tomato': '番茄'
}

# Added on 2019/03/15
category_list = list(category_zh_dict.keys())
category_set = set(category_zh_dict.keys())

# Added on 2019/03/15
cat_to_labels_dict = {
    'apple': ['0', '1', '2', '3', '4', '5'],
    'cherry': ['6', '7', '8'],
    'corn': ['10', '11', '12', '13', '14', '15', '16', '9'],
    'grape': ['17', '18', '19', '20', '21', '22', '23'],
    'citrus': ['24', '25', '26'],
    'peach': ['27', '28', '29'],
    'pepper': ['30', '31', '32'],
    'potato': ['33', '34', '35', '36', '37'],
    'strawberry': ['38', '39', '40'],
    'tomato': ['41','42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', \
                '53', '54', '55', '56', '57', '58', '59', '60']
}


# Added on 2019/03/08
def is_image_file(path):
    """
    Check if the file at 'path' is a valid image file by suffix

    Arguments
        path : (str) file's full path.

    Returns 
        (bool) : True if it's a valid image file, else False.

    """
    valid_img_suffix = ('jpg', 'jpeg', 'png')
    if path.rsplit('.', 1)[1].lower() in valid_img_suffix and not path.startswith('.'):
        return True
    else:
        print('"%s" is not a valid image file' % path)
        return False


# Added on 2019/03/14
def check_plt_filename(filename):
    """
    Assert the suffix of the input plt_name

    Arguments
        filename: (str) plot file name to be checked.

    Returns
        suffix: (str) suffix of the filename if it's valid, None if not valid

    """
    if len(filename.rsplit('.', 1)) == 1:
        raise Exception('[KF ERROR] save_name "%s" is not a valid filename.' % filename)
    suffix = filename.rsplit('.', 1)[1].lower()
    if not suffix in ('jpg', 'png', 'eps'):
        raise Exception('[KF ERROR] save_name suffix "%s" is not a valid plot format.' % suffix)
    return suffix


# Added on 2019/03/11
def plot_distribution(x, height, label='data', title='Data Distribution', save_dir='.', filename='data-distribution.eps'):
    """
    Plot data distribtuion of a given dataset. 
    Put numbers for each category on top of bars.

    Arguments
        x : (list) x coordinate of the bar
        height : (list) height(s) of the bar(s).
        title : (str) figure title.
        filename : (str) filename to be saved.

    Returns
        None

    """
    plt.figure(figsize=(8,6))
    color = 'dodgerblue'
    plt.bar(x, height, width = 0.75, color=color, label=label)
    offset = 0

    for i in range(len(x)):
        xy = (i, height[i]+ offset)
        plt.annotate('%d' % xy[1], xy=xy, textcoords='data', horizontalalignment='center', color='gray', weight='bold')
    
    plt.grid(axis='y', ls='--', lw=.5, c='lightgray')
    plt.xticks(x)
    plt.title(title)
    plt.legend()
    suffix = check_plt_filename(filename)
    plt.savefig(os.path.join(save_dir, filename), format=suffix, dpi=1000)
    print('[KF INFO] Data distribution plot is saved as "%s"!' % filename)
    

# Added on 2019/03/11
def print_title(title, symbol='=', f=None):
    """
    Print title with double lines with text aligned to center.
    
    Arguments
        title : (str) Title string to be printed.
        f : (file obj) if f is not None, write the printed content to the file.
        line : (str) The symbol for printing lines.

    Returns
        None

    """
    width = 80
    print('', file=f)
    if len(symbol):
        print(symbol * width, file=f)
    print(' ' * ((width - len(title))//2 - 1), title, file=f)
    if len(symbol):
        print(symbol * width, file=f)


# Added on 2019/03/12
# Modified on 2019/03/14
def plot_loss_acc(history, save_dir, filename='plt-acc-loss.eps', title='Accuracy and Loss'):
    """
    Plot valloss, loss, val_acc and acc in 

    Arguments
        history : (dict) H.history where H is the return of model.fit()
        save_dir : (str) save directory (relative)

    Returns
        None

    """
    suffix = check_plt_filename(filename)

    N = len(history["loss"])
    #plt.style.use("ggplot")
    #plt.figure()
    fig, ax1 = plt.subplots(figsize=(8, 6))
    ax2 = ax1.twinx()
    #N = epochs
    l1 = ax1.plot(np.arange(0, N), history["acc"], label="train_acc")
    l2 = ax1.plot(np.arange(0, N), history["val_acc"], label="val_acc", linewidth=2)
    ax1.set_ylabel('Accuracy')
    ax1.set_xlabel('Epoch #')
    ax1.set_ylim(0, 1.05)
    ax1.grid()

    l3 = ax2.plot(np.arange(0, N), history["loss"], color='orchid', linestyle='dashed', label="train_loss")
    l4 = ax2.plot(np.arange(0, N), history["val_loss"], color='limegreen', linestyle='dashed', label="val_loss", linewidth=2)
    ax2.set_ylabel('Loss')
    # Put all label legend together
    l = l1 + l2 + l3 + l4
    labels = [i.get_label() for i in l]
    plt.legend(l, labels, loc='center right')
    if title != 'Accuracy and Loss':
        title = 'Accuracy and Loss - ' + title
    plt.title(title)

    best_val_acc = max(history['val_acc'])
    # Save best val_acc into filename
    filename = '.'.join([filename.rsplit('.')[0] + '-%.4f' % best_val_acc, suffix])
    
    plt.savefig(os.path.join(save_dir, filename), format=suffix, dpi=1000)
    print('[KF INFO] Loss and acc history is plotted and saved as "%s"!' % filename)


# Added on 2019/03/12
# Modified on 2019/03/14
def plot_lr(history, save_dir, filename='plt-lr.eps', title='Learning Rate'):
    """
    Plot Learning Rate`

    Arguments
        history : (dict) H.history where H is the return of model.fit()
        save_dir : (str) save directory (relative)

    Returns:
        None

    """
    suffix = check_plt_filename(filename)

    N = len(history["lr"])
    plt.figure(figsize=(8, 6))
    plt.plot(np.arange(0, N), history['lr'], linewidth=4)
    plt.xlabel('Epoch #')
    plt.ylabel('Learning Rate')
    plt.grid()
    if title != 'Learning Rate':
        title = 'Learning Rate - ' + title
    plt.title(title)
    plt.savefig(os.path.join(save_dir, filename), format=suffix, dpi=1000)
    print('[KF INFO] Learning rate history is plotted and saved as "%s"!' % filename)


# Tests
if (__name__ == "__main__"):
    
    print_title('Test %s' % __file__, symbol='*')
    # Test 'is_image_file'
    #print("[KF INFO] Test is_image_file()")
    #print("-"*80)
    #li = ['._abcd.JPG', 'cbd.jpeg', '.DSTORE', 'bd3e.png']
    #for f in li:
    #    print(is_image_file(f))

    # Test 'plot_distribution'
    #x = [i for i in '中文标题']
    #height = [40,50,60,20]
    #label = '中文标签'
    #title = '中文标题'
    #plot_distribution(x, height, label, title=title, filename='try-data-dist.png')
    # Test Passed! - KF 2019/03/11

    # Test 'plot_distribution'
    #h = {}
    #h['loss'] = np.array([4,3,2,1,0.5])
    #h['val_loss'] = np.array([4,3,2,1,0.5])*0.9
    #h['acc'] = np.array([50, 60, 70, 80, 90])*.01
    #h['val_acc'] = (np.array([50, 60, 70, 90, 80]) - 3)*.01
    #h['lr'] = np.array([1e-4, 1e-4, 5e-5, 5e-5, 2.5e-5])
    #print(h)
    #plot_loss_acc(h, '.', 'abcd.eps', 'asdfasdf adf zxcvz cv')
    #plot_lr(h, '.', 'efg.png', 'hello world')

    # test print_title with argument 'f'
    # with open('try.txt', 'a') as f:
    #    print_title("HEllo world!", f=f)
    # Test Passed!
    
    #print(category_list)
