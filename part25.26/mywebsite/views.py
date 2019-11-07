from django.shortcuts import render


def index(request):
	dict = {
	'judul':'Home Page',
	'content':'ini adalah home dari website ini',

	}

	return render(request,'index.html',dict)