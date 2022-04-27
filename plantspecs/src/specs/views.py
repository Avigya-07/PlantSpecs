from dataclasses import fields
from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render
from . import models
from specs.models import plant, Area, Treatment
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
import tensorflow as tf
import keras
from keras.preprocessing import image
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from tensorflow import Graph
import json
import numpy as np
# Create your views here.


img_height,img_width=180,180
# with open('./models/labels_string.json','r') as f:
#     labelInfo=f.read()

# labelInfo=json.loads(labelInfo)
class_names=['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model=load_model('models/new_model.h5')


def index(request):
    context={'a':1}
    return render(request,'Homepage.html',context)

def information(request):
    Plants=plant.objects.all()
    Areas=Area.objects.all()
    Treat=Treatment.objects.all()

    context={
        'Plants': Plants,
        'Areas':Areas,
        'Treat':Treat
    }
    return render(request,'Information.html',context)

def PredictImage(request):
    print (request)
    print (request.POST.dict())
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    testimage='.'+filePathName
    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x=x/255
    x=x.reshape(1,img_height, img_width,3)
    with model_graph.as_default():
        with tf_session.as_default():
            predi=model.predict(x)
            score = tf.nn.softmax(predi[0])
            label=class_names[int(np.argmax(score))]
            accuracy=np.max(score)
            

    # predictedLabel=class_names[int(np.argmax(predi[0]))]
    # predictedLabel=class_names[np.argmax(predi[0])]
    #   'predictedLabel':predictedLabel
    context={'filePathName':filePathName,'accuracy':accuracy}
    return render(request,'Homepage.html',context)
