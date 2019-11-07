from django.shortcuts import render

# Create your views here.


def khusus(request, input):
	dict = {
		'judul': input,

	}

	return render (request,'blog/index.html',dict)


def categoryPost(request):
	dict = {
		'judul': 'category post',

	}

	return render (request,'blog/index.html',dict)

def singlePost(request):
	dict = {
		'judul': 'single post',

	}

	return render (request,'blog/index.html',dict)

def index(request):
	dict = {
		'judul': 'home blog',

	}

	return render (request,'blog/index.html',dict)