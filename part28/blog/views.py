from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
	Posts = Post.objects.all();
	categories = Post.objects.values('category').distinct();
	dict = {
		'judul':'Home Blog',
		'content':'ini adalah home dari blog',
		'Categories':categories,
		'posts' : Posts,

	}

	return render(request,'blog/index.html',dict)

def categoryPost(request, dataCategory):
	Posts = Post.objects.filter(category=dataCategory);
	

	categories = Post.objects.values('category').distinct();

	dict = {
		'judul':'Home Blog',
		'content':'ini adalah home dari blog',
		'Categories':categories,
		'posts' : Posts,

	}

	return render(request,'blog/category.html',dict)


def detailPost(request, inputSlug):
	Posts = Post.objects.get(slug = inputSlug);
	categories = Post.objects.values('category').distinct();
	dict = {
		'judul':'Home Blog',
		'content':'ini adalah home dari blog',
		'Categories':categories,
		'posts' : Posts,

	}

	return render(request,'blog/detail.html',dict)