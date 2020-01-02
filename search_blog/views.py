from django.shortcuts import render
from posts.models import Post

# Create your views here.
def do_search_blog(request):
    posts = Post.objects.filter(title__icontains=request.GET['q'])
    return render(request, 'blogposts.html', {'posts':posts})