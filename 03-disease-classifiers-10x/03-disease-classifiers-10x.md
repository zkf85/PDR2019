# 【开发文档】10个类内病虫害分类器
*（2019/03/12)*

> **说明：** 该模块的目的是在已经确定作物类别之后，判断具体是哪一种病虫害的10个分类器。该模块的输入为用户采集的图像（已确定类别)，输出为预测的**病虫害**类别。
> 
> **模块路径：**
> `kefeng@aizhong-ubuntu-server:~/2019-PlantDiseaseRecognition-v2/03-disease-classifiers-10x`
> 

## 0. 开发流程概述
1. 数据整理——将原始数据集根据`label_to_disease_full.json`按照作物类别重新整理。训练集、验证集划分。
2. 对于每一个作物类别分别进行以下步骤：
    1. 数据分析——数据均衡、数据增强。
    2. 训练模型。
    3. 模型性能分析。

## 1. 数据整理
*(2019/03/13)*
### 1.1. 生成类别-标签对应表
脚本：`01-generate-category-to-folders-dict.py`
输出文件：`cat-to-folders.json`

### 1.2. 重新整理、拷贝数据集
> **为什么？**
> 
> 因为用keras的flow_from_directory的时候，会自动将目录下的所有文件夹默认识别为各个类别标签。所以要按照不同作物类别将原始数据集重新分类。

脚本：`02-rearrange-and-copy-dataset.py`
输入：上一个脚本的生成文件`cat-to-folders.json`
输出：整理后的新数据集文件夹位置及拓扑：
```
/home/kefeng/data_pool/plant_disease_dataset/dataset_for_10x_classifiers/
├── apple
│   ├── concat
│   │   ├── 0
│   │   ├── 1
│   │   ├── 2
│   │   ├── 3
│   │   ├── 4
│   │   └── 5
│   ├── train
│   │   ├── 0
│   │   ├── 1
│   │   ├── 2
│   │   ├── 3
│   │   ├── 4
│   │   └── 5
│   └── val
│       ├── 0
│       ├── 1
│       ├── 2
│       ├── 3
│       ├── 4
│       └── 5
├── cherry
│   ├── concat
│   │   ├── 6
│   │   ├── 7
│   │   └── 8
│   ├── train
│   │   ├── 6
│   │   ├── 7
│   │   └── 8
│   └── val
│       ├── 6
│       ├── 7
│       └── 8
...
```

## 2. 模型训练
### 2.1. 苹果（apple）
