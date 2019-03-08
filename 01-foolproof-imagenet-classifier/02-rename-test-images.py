# KF 03/08/2019
# Rename all images in the test-image directory by beginning with 001.jpg and so on
import os
test_dir = 'general-test-images'

# Find all image file in test_dir
f_list = [i for i in os.listdir(test_dir) if not i.startswith('.') and i.rsplit('.', 1)[-1].lower() in ('jpg', 'png', 'jpeg')]
print('[KF INFO] files to be renamed:')
print(f_list)

def format_img_suffix(suffix):
    """
    Reformat the image file suffix string to uniform type:
    Example:
        input: 'JPG'  -> output: 'jpg'
        input: 'jpeg' -> output: 'jpg'
        input: 'PNG'  -> output: 'png'
    Return:
        Reformatted suffix string
    """
    jpg = ('jpg', 'jpeg')
    png = ('png',)
    if suffix.lower() in jpg:
        return 'jpg'
    elif suffix.lower() in png:
        return 'png'

# Renameing loop:
for i, f in enumerate(sorted(f_list)):
    [f_name, suffix] = f.rsplit('.', 1)
    suffix = format_img_suffix(suffix)
    
    dist = str(i+1).zfill(4) + '.' + suffix
    os.rename(os.path.join(test_dir, f), os.path.join(test_dir, dist))
    print('%s is renamed as: %s' % (f, dist))

