# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from news.models import NewsModel

def index(request):
    """
    首页
    """
    news_list = NewsModel.objects.all()
    return render(request, 'index.html',context={'news_list':news_list})


def add_news(request):
    """
    添加新闻
    """
    if request.method == 'GET':
        return render(request,'add_news.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        news_model = NewsModel(title=title, content=content)
        news_model.save()
        return redirect('index')

def news_detail(request,news_id):
    """
    新闻详情
    """
    news_model = NewsModel.objects.filter(id=news_id).first()
    return render(request,'')