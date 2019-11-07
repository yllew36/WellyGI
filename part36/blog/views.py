from django.shortcuts import render, redirect

# Create your views here.

from .forms import PostForm
from .models import Post

def index(request):
	posts = Post.objects.all()

	dict	= {
		'page_title':'post list',
		'posts':posts,
	}
	return render (request,'blog/index.html',dict)

def create(request):
	post_form = PostForm(request.POST or None)

	if request.method == 'POST':
		if post_form.is_valid():
			# Post.objects.create(
			# 	judul		= request.POST.get('judul'),
			# 	body		= request.POST.get('body'),
			# 	category	= request.POST.get('category'),
			# 	)

			post_form.save()
			return redirect('blog:index')

	dict	= {
		'post_title':'create post',
		'post_form':post_form,
	}
	return render (request,'blog/create.html',dict)