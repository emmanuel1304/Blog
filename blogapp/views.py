
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage 
from django.shortcuts import render
from .models import Post, Catagory

def post_list(request):
    posts = Post.objects.filter(status='published')
    paginator = Paginator(posts, 1) # 10 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    categories = Catagory.objects.all()
    featured = Post.objects.filter(featured=True)
    breaking_news = Post.objects.filter(breaking_news=True)
    return render(request,'blogapp/index.html',context={'posts':posts, 'categories': categories, 'featured': featured, 'breaking_news': breaking_news, 'page':page})


def post_detail(request, id):
    post=Post.objects.get(id=id)
    return render(request, 'blogapp/blog-detail.html',context={'post':post})    