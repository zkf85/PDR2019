# KF 2019/03/08
# Utility Methods 
import os

def is_image_file(path):
    """
    Check if the file at 'path' is a valid image file by suffix
    by KF 2019/03/08
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


if (__name__ == "__main__"):
    
    print("="*80)
    print("[KF INFO] Start testing module utils.py")
    print("="*80)

    print("[KF INFO] Test is_image_file()")
    print("-"*80)
    li = ['abcd.JPG', 'cbd.jpeg', '.DSTORE', 'bd3e.png']
    for f in li:
        print(is_image_file(f))

        
    
