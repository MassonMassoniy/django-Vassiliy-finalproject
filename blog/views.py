from django.shortcuts import render
from blog.models import Post, AboutUs


def index(request):
    ls=Post.objects.all()
    return render(request,'index.html',{'posts':ls})


def about(request):
    about = AboutUs.objects.last()
    # AboutUs.objects.get()
    # AboutUs.objects.filter()
    return render(request,'about.html',{'about':about})
# Create your views here.
