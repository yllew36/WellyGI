from django.shortcuts import render


def index(request):
	dict	= {
		'page_title':'Home Website',
		'content':'Ini adalah halaman home'
	}
	return render(request,'index.html',dict)