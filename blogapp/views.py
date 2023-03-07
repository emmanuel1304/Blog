
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage 
from django.shortcuts import render
from .models import Post, Catagory, Comment
from .forms import CommentForm

def post_list(request):
    posts = Post.objects.filter(status='published')
    
    categories = Catagory.objects.all()
    featured = Post.objects.filter(featured=True)
    breaking_news = Post.objects.filter(breaking_news=True)
    return render(request,'blogapp/index.html',context={'posts':posts, 'categories': categories, 'featured': featured, 'breaking_news': breaking_news,})


def post_detail(request, id):
    post=Post.objects.get(id=id)
    
    return render(request, 'blogapp/blog-detail.html',context={'post':post,})    

# handling reply, reply view
def reply_page(request):
    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():
            post_id = request.POST.get('post_id')  # from hidden input
            parent_id = request.POST.get('parent')  # from hidden input
            post_url = request.POST.get('post_url')  # from hidden input

            reply = form.save(commit=False)
    
            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.save()

            return redirect(post_url+'#'+str(reply.id))

    return redirect("/")    