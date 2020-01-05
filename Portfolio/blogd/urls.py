from django.urls import path,include
from blogd.views import Blogd
urlpatterns = [
    path("",Blogd)
]