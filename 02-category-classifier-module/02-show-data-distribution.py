# 2019/03/11
# Show data distribution of categorical plan disease data
import os
import json
from utils import is_image_file, plot_distribution
from utils import category_zh_dict as cat_dict
#===============================================================================
# 1. paths
#===============================================================================
base_dir = '/home/kefeng/data_pool/plant_disease_dataset/dataset_plant_categorical'

#===============================================================================
# 2. Plotting
#===============================================================================
subdirs = os.listdir(base_dir)

for subdir in subdirs:
    print(subdir)
    cats = sorted(os.listdir(os.path.join(base_dir, subdir)))
    counts = []
    for cat in cats:
        ct = [i for i in os.listdir(os.path.join(base_dir, subdir, cat)) if is_image_file(i)] 
        counts.append(len(ct))

    with open('dist-%s.json' % subdir, 'w') as f:
        json.dump([cats, counts], f, indent=4)

    # Plot data distributions
    cats_zh = [cat_dict[i] for i in cats]
    print(cats_zh)
    title = '作物图片样本分布 - %s' % subdir.capitalize()
    #filename = '02-data-distribution-%s.eps' % subdir  # problem rendering chinese in eps mode
    filename = '02-data-distribution-%s.png' % subdir
    plot_distribution(cats_zh, counts, label=subdir, title= title, filename=filename)
    
