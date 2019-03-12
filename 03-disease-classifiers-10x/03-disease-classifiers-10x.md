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
### 1.1. 数据集
原始数据集存储路径：
```
kefeng@aizhong-ubuntu-server:
~/data_pool/plant_disease_dataset
├── 299_dataset_for_keras
├── dataset
└── dataset_for_keras
```
- `299_dataset_for_keras` 为尺寸统一为299x299的按61类整理的数据；
- `dataset`为原始数据；
- `dataset_for_keras`为原始尺寸的按61类整理的数据。

这些数据是2018年11月初参与竞赛时所整理。当前项目的数据整理，同样使用`dataset_for_keras`的数据作为初始数据。

### 1.2. 将数据按照作物类别整理成为新的副本
**目标：**
- 将原始数据集文件夹（"0", "1", ...)按照所属类别进行整理，目标文件夹拓扑如下：
```
~/data_pool/plant_disease_dataset/dataset_plant_disease_10x

```

**程序脚本：**
- `01-rearrange-dataset.py` 主脚本
- `kfutils.py` 功能函数

处理完成后的数据文件夹结构：
```
~/data_pool/plant_disease_dataset/dataset_plant_categorial                                                   
├── concat
│   ├── apple
│   ├── cherry
│   ├── citrus
│   ├── corn
│   ├── grape
│   ├── peach
│   ├── pepper
│   ├── potato
│   ├── strawberry
│   └── tomato
├── train
│   ├── apple
│   ├── cherry
│   ├── citrus
│   ├── corn
│   ├── grape
│   ├── peach
│   ├── pepper
│   ├── potato
│   ├── strawberry
│   └── tomato
└── val
    ├── apple
    ├── cherry
    ├── citrus
    ├── corn
    ├── grape
    ├── peach
    ├── pepper
    ├── potato
    ├── strawberry
    └── tomato
```

***【完成 2019/03/08】***

### 1.3. 训练集、验证集划分
本部分已经在`01-rearrange-dataset.py`中同时完成。
数据概览：
- 总图片数：36258
- 训练集图片数：31718
- 验证集图片数：4540

## 2. 数据分析
### 2.1. 按类别的数据分布（共10类）
脚本：`02-data-distribution.py`

![](02-data-distribution-concat.png)
![](02-data-distribution-train.png)
![](02-data-distribution-val.png)

### 2.2. 数据增强（Data Augmentation）
考虑效率问题，目前直接使用Keras的实时图像增强。

## 3. 模型、训练
*(2019/03/11)*
脚本：
```
~/2019-PlantDiseaseRecognition-v2/02-category-classifier-module/
├── 03-train.py     # main entry
├── model.py        # model
├── config.py       # parameters and paths
```
### 3.1. 训练脚本完成，开始第一轮训练：
*(2019/03/12)*
模型文件夹：`20190312-model-InceptionResNetV2-epochs-20-batchsize-8`
模型指标：
- train_acc:
- val_acc: 