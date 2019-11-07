from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
	semuapost = Post.objects.all();


	dict = {
	'Title':'Blog',
	'Heading':'Selamat Datang di Blog',
	'Category':'All',
	'Posts':semuapost,
	}

	return render(request,'index.html',dict)

def jurnal(request):
	semuapost = Post.objects.filter(category ='Jurnal');


	dict = {
	'Title':'Blog',
	'Heading':'Selamat Datang di Blog',
	'Category':'Jurnal',
	'Posts':semuapost,
	}

	return render(request,'index.html',dict)

def berita(request):
	semuapost = Post.objects.filter(category ='Berita');


	dict = {
	'Title':'Blog',
	'Heading':'Selamat Datang di Blog',
	'Category':'Berita',
	'Posts':semuapost,
	}

	return render(request,'index.html',dict)

def gosip(request):
	semuapost = Post.objects.filter(category ='Gosip');


	dict = {
	'Title':'Blog',
	'Heading':'Selamat Datang di Blog',
	'Category':'Gosip',
	'Posts':semuapost,
	}

	return render(request,'index.html',dict)
