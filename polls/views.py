# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import apple_keras as apple


image_size = 32
categories = ["シュワッ", "フォフォフォフォ"]

def index(request):
    return render(request, 'polls/index.html',{'ans':'お試し'})

def manval(request):
    try:
        X = []
        text=request.POST['manval']
        img = request.FILES['file']
        
        in_data = img_to_array(img)
        X.append(in_data)
        X = np.array(X)
        X  = X.astype("float")  / 256
    
        model = apple.build_model(X.shape[1:])
        model.load_weights("./image/apple-model.h5")
    
        pre = model.predict(X)
        print(pre)
        if pre[0][0] > 0.9:
            #print(categories[0])
            text = 'これは' + categories[0]+ 'だよ'
            #text = text.encode('utf-8')
            #jtalk(text)
        elif pre[0][1] > 0.9:
            #print(categories[1])
            text = 'これは' + categories[1]+ 'だよ'
            #text = text.encode('utf-8')
                #jtalk(text)
        
        else:
            text = '該当なし'
    
        print(text)
    except (KeyError):
        return render(request, 'polls/index.html',{'ans':'お試し'})
    else:
        return render(request, 'polls/index.html',{'ans':text})