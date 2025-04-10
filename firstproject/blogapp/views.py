from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'home.html')

def post_create(request):
    
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        Post.objects.create(author=author, title=title, content=content)
        return redirect('home')
    return render(request, 'create.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})