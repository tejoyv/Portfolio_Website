from django.shortcuts import render
from .models import Blog
# Create your views here.

def Blogg(request):
	blog=Blog.objects
	return render(request,'blog.html',{'all_blogs':blog})
