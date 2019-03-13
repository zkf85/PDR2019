"""
Filename: 01-generate-category-to-folders-dict.py 
Created on Wed Mar 13 10:51:55 CST 2019

@author: Kefeng Zhu (zkf1985@gmail.com, zkf85@163.com)

Description:
  Generate a dictionary:
  - key   : (str)  category, e.g. 'apple', 'tomato'
  - value : (list) a sorted list of folder names (str), e.g. "['0', '1', '2']"
  - save the dictionary as a JSON file 
    "cat-to-folders.json"

  'label_to_disease_full.json' is needed.

"""
import os
import json

#base_dir = '/home/kefeng/data_pool/plant_disease_dataset/dataset_for_keras/concat'

# load 'label_to_disease_full.json'
with open('../label_to_disease_full.json', 'r') as f:
    l = json.load(f)
    #print(l)

def gen_dict(l):
    dic = {}
    for slot in l:
        if not dic.get(slot[1]):
            dic[slot[1]] = set()
        dic[slot[1]].add(str(slot[0]))

    for k in dic.keys():
        dic[k] = sorted(dic[k])
    print(dic)
    with open('cat-to-folders.json', 'w') as f:
        json.dump(dic, f, indent=4)



if __name__ == "__main__":
    gen_dict(l)



