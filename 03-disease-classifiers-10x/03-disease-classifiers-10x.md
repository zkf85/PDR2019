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
脚本：
```
03-disease-classifiers-10x/
└── 01-generate-category-to-folders-dict.py
```

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
### 2.1. 模型训练脚本：
```
2019-PlantDiseaseRecognition-v2/
├── utils.py            # 常用功能函数
├── model.py            # 构建模型函数
└── 03-disease-classifiers-10x/     
    ├── 03-train-children.py    # 训练主程
    └── config.py               # 参数文件
```

#### TODO (2019/03/14)
将参数与python脚本彻底分离，拟采用json文件存储参数

### 2.2. 训练结果与分析
#### 2.2.1. VGG16 (10个模型)
*(2019/03/14)*
### 统一训练参数：
```
Model Name       : VGG16
Image Shape      : (224, 224, 3)
--------------------------------------------------------------------------------
Train Size       : 11476
Validation Size  : 1639
--------------------------------------------------------------------------------
Epochs           : 50
Batch Size       : 16
Initial LR       : 0.0001
Early Stopping Patience  : 20
LR Reduce Patience       : 8
```
### 模型准确率与损失函数：
| ![](plots/20190313-apple-plt-acc-loss.eps) | ![](plots/20190313-cherry-plt-acc-loss.eps) |
| :-: | :-: |
| 苹果: 94.74% | 樱桃: 99.11% |

| ![](plots/20190313-citrus-plt-acc-loss.eps) | ![](plots/20190313-corn-plt-acc-loss.eps) |
| :-: | :-: |
| 桔子: 75.00% | 玉米: 87.73% |

| ![](plots/20190313-grape-plt-acc-loss.eps) | ![](plots/20190313-peach-plt-acc-loss.eps) |
| :-: | :-: |
| 葡萄: 86.98% | 桃子: 90.62% |

| ![](plots/20190313-pepper-plt-acc-loss.eps) | ![](plots/20190313-potato-plt-acc-loss.eps) |
| :-: | :-: |
| 辣椒: 95.00% | 土豆: 85.11% |

| ![](plots/20190314-strawberry-plt-acc-loss.eps) | ![](plots/20190314-tomato-plt-acc-loss.eps) |
| :-: | :-: |
| 草莓: 93.75% | 番茄: 85.11% |
