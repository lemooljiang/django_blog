from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from blog import models
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
import json



# Create your views here.

category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')

def index(request):
    category_obj = models.Category.objects.get(position_index=1)
    article_list = models.Article.objects.filter(status='published')
    return render(request,'index.html',{'category_list':category_list,
                                            'article_list':article_list,
                                             'category_obj':category_obj,
                                            })

def category(request,id):
    category_obj = models.Category.objects.get(id=id)
    if category_obj.position_index == 1:#首页
        article_list = models.Article.objects.filter(status='published')
    else:
        article_list = models.Article.objects.filter(category_id = category_obj.id,status='published')
    return render(request,'index.html',{'category_list':category_list,
                                            'category_obj':category_obj,
                                            'article_list':article_list
                                            })


def article_detail(request,article_id):
    article_obj = models.Article.objects.get(id=article_id)
    return render(request,'article_detail.html',{'article_obj':article_obj,
                                                     'category_list':category_list,})
