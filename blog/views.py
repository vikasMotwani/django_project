from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    context = {'posts' : Post.objects.all()}
    #return HttpResponse('<h1>Home</h1>')
    return render(request, 'home.html', context)

def about(request):
    #return HttpResponse('<h1>About</h1>')
    return render(request, 'about.html', {'title': 'About'})