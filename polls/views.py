# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'polls/index.html',{'ans':'お試し'})

def manval(request):
    try:
        text=request.POST['manval']
    except (KeyError):
        return render(request, 'polls/index.html',{'ans':'失敗'})
    else:
        return render(request, 'polls/index.html',{'ans':text})