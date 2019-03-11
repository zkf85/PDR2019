# Created by KF 
# 2019/03/08
# Utility Methods 
import os

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
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei']    # 正常显示标签
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 正常显示标签
#plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号
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
def print_title(title):
    width = 80
    print('')
    print('=' * width)
    print(' ' * ((width- len(title))//2 - 1), title)
    print('=' * width)



################################################################################
# Main entry, for testing
################################################################################
if (__name__ == "__main__"):
    
    print("="*80)
    print("[KF INFO] Start testing module utils.py")
    print("="*80)

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



