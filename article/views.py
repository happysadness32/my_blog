from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Article

from datetime import datetime
from django.http import Http404

def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{"post_list":post_list})

def detail(request,id):
    try:
        post = Article.objects.all().filter(id=id)[0]

    except IndexError:
        raise Http404
    #两种写法，get获取到的是一个对象，filter获取的是一个列表
    # try:
    #     post = Article.objects.all().get(id=0)
    #
    # except Article.DoesNotExist:
    #     raise Http404
    return render(request, 'post.html',{"post":post})

