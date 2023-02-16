from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.

from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request,'blogapp/index.html',context={'posts':posts})


def post_detail(request, post):
    post=get_object_or_404(Post,slug=post,status='published')
    return render(request, 'post_detail.html',context={'post':post})    