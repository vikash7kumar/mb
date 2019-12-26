from django.shortcuts import render
from django.views.generic import ListView
from testapp.models import Post
# Create your views here.
class Home_view(ListView):
    model=Post
    template_name="testapp/home.html"
    context_object_name="Post_list"
