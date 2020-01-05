from django.urls import path,include
from blog.views import Blogg
urlpatterns = [
    path("",Blogg),
]