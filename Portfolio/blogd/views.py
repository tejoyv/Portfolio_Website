from django.shortcuts import render
from blog.models import Blog
# Create your views here.
def Blogd(request):
	blog=Blog.objects
	return render(request,'blogd.html',{'all_blogs':blog})