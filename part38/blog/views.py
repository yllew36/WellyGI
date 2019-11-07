from django.shortcuts import render, redirect

# Create your views here.
from .forms import PostForm
from .models import PostModel

def list(request):
	posts	= PostModel.objects.all()

	dict= {
		'page_title':'Semua Post',
		'posts':posts
	}
	return render (request,'blog/list.html',dict)


def create(request):
	post_form = PostForm(request.POST or None)

	if request.method =='POST':
		if post_form.is_valid():
			post_form.save()

			return redirect('blog:list')

	dict = {
		'page_title':'Create Post',
		'post_form':post_form,

	}

	return render (request,'blog/create.html',dict)