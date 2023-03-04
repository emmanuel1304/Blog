
from django.shortcuts import render, get_object_or_404
# Create your views here.

from django.shortcuts import render
from .models import Post, Catagory

def post_list(request):
    posts = Post.objects.filter(status='published')
    categories = Catagory.objects.all()
    featured = Post.objects.filter(featured=True)
    breaking_news = Post.objects.filter(breaking_news=True)
    return render(request,'blogapp/index.html',context={'posts':posts, 'categories': categories, 'featured': featured, 'breaking_news': breaking_news})


def post_detail(request, id):
    post=Post.objects.get(id=id)
    return render(request, 'blogapp/blog-detail.html',context={'post':post})    