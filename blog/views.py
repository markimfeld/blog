from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-pub_date')
	template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

