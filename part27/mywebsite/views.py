from django.shortcuts import render


def index(request):
	dict = {
	'judul': 'home my website',

	}

	return render(request,'index.html',dict)