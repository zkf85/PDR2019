"""
Filename: pdr_serve.py 
Created on Fri Mar 15 17:19:22 CST 2019

@author: Kefeng Zhu (zkf1985@gmail.com, zkf85@163.com)

== Plant Disease Recognition (PDR) ==
Serve as API

"""
import flask
from flask import Flask, request, Response

from tensorflow.keras.models import load_model

#from predict import predict

# Initialize Flask application
#app = Flask(__name__)

def pdr_init():
    """
    Initialize PDR: load models 

    """
    # Paths
    model_base_dir = '/home/kefeng/model_pool/plant_disease_recognition_models/pdr_deploy_models' 

    names = [n for n in os.listdir(model_base_dir) if not n.startswith('.') and os.path.isdir(n)]
    print(names)
    

if __name__ == "__main__":
    pdr_init()
    



