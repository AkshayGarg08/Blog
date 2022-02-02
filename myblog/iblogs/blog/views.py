from django.shortcuts import render
from .models import *
# from django.http import HttpResponse

# function based views here.
def home(request):
    '''load all the post from db here(10)'''
    posts = Post.objects.all()#[:11]
    cats = Category.objects.all()
    context = {
        'pos':posts,
        'cats':cats
    }
    return render(request,'home.html',context)


def detailpost(request,url):
    posts = Post.objects.get(url=url)
    cats = Category.objects.all()
    context = {'pos':posts, 'cats':cats}
    return render(request,'posts.html',context)

def category(request,url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    context = {'cat':cat, 'posts':posts}
    
    return render(request,'category.html',context)

def about(request):
    return render(request,'about.html',{})










