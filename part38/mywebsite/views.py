from django.shortcuts import render


def index(request):
	dict = {
		'page_title':'Home'
	}
	return render(request,'index.html', dict)