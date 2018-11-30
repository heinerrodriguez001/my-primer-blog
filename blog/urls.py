

from django.conf.urls import url
from . import views
from django.shortcuts import render, get_object_or_404

def post_detail (request, pk):
	Post.objects.get(pk=pk)

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

