from django.shortcuts import render

def index(request):
	dict = {
		'heading':'Home',
		'content':'ini adalah home',
	}
	return render(request,'index.html',dict)