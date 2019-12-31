from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

# Create your views here.

def get_posts(request):
    """
    Creates view that will return list
    of Posts, renders to the 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID, then
    renders it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})
