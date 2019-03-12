# Created by KF 
# 2019/03/08
# Utility Methods 
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei']    # 正常显示标签
#plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 正常显示标签
#plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号
import numpy as np

# Added by KF 2019/03/11
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

#===============================================================================
# Added by KF 
# 2019/03/08
#===============================================================================
def is_image_file(path):
    """
    Check if the file at 'path' is a valid image file by suffix
    Input:
        - path: (str) file's full path

    Return: 
        True if it's a valid image file.
    """
    valid_img_suffix = ('jpg', 'jpeg', 'png')
    if path.rsplit('.', 1)[1].lower() in valid_img_suffix:
        return True
    else:
        print("%s is not a valid image file" % path)
        return False

#===============================================================================
# Added by KF
# 2019/03/11
#===============================================================================
def plot_distribution(x, height, label='data', title='Data Distribution', savedir='.', filename='data-distribution.eps'):
    """
    Plot data distribtuion of a given dataset. 
    Feature: put numbers for each category on top of bars.

    Input:
        x: (list) x coordinate of the bar
        height: (list) height(s) of the bar(s).
        title: (str) figure title.
        filename: (str) filename to be saved.

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
    suffix = filename.rsplit('.', 1)[1].lower()
    plt.savefig(os.path.join(savedir, filename), format=suffix, dpi=1000)
    print('[KF INFO] %s is saved!' % filename)
    

#===============================================================================
# Print title with double lines with text aligned to center
# Added by KF 2019/03/11
#===============================================================================
def print_title(title, f=None):
    width = 80
    print('', file=f)
    print('=' * width, file=f)
    print(' ' * ((width - len(title))//2 - 1), title, file=f)
    print('=' * width, file=f)

#===============================================================================
# Plot valloss, loss, val_acc and acc in 
# Added by KF 2019/03/12
#===============================================================================
def plot_loss_acc(history, save_dir):
    """
    Arguments:
        history: (dict) H.history where H is the return of model.fit()
        save_dir: (str) save directory (relative)
    """
    print_title("Plot the Loss and Accuracy")
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
    plt.title("Training Loss and Accuracy")
    plt_name = 'plt-acc-loss.eps'
    plt.savefig(os.path.join(save_dir, plt_name), format='eps', dpi=1000)

#===============================================================================
# Plot Learning Rate`
# Added by KF 2019/03/12
#===============================================================================
def plot_lr(history, save_dir):
    """
    Arguments:
        history: (dict) H.history where H is the return of model.fit()
        save_dir: (str) save directory (relative)
    """
    print_title("Plot Learning Rate")
    N = len(history["lr"])
    plt.figure(figsize=(8, 6))
    plt.plot(np.arange(0, N), history['lr'], linewidth=4)
    plt.xlabel('Epoch #')
    plt.ylabel('Learning Rate')
    plt.grid()
    plt.title("Learning Rate")
    plt_name = 'plt-lr.eps'
    plt.savefig(os.path.join(save_dir, plt_name), format='eps', dpi=1000)


################################################################################
# Main entry, for testing
################################################################################
if (__name__ == "__main__"):
    
    print("[KF INFO] Start testing module utils.py")
    # Test 'is_image_file'
    #print("[KF INFO] Test is_image_file()")
    #print("-"*80)
    #li = ['abcd.JPG', 'cbd.jpeg', '.DSTORE', 'bd3e.png']
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
    #h['val_acc'] = (np.array([50, 60, 70, 80, 90]) - 3)*.01
    #h['lr'] = np.array([1e-4, 1e-4, 5e-5, 5e-5, 2.5e-5])
    #print(h)
    #plot_loss_acc(h, '.')
    #plot_lr(h, '.')

    # test print_title with argument 'f'
    # with open('try.txt', 'a') as f:
    #    print_title("HEllo world!", f=f)
    # Test Passed!
    
