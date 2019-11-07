from django.shortcuts import render

def index(request):
	dict = {
	'title':'About',
	'heading':'About',
	'subheading':'Tentang Kelas Terbuka',
	}
	return render(request,'about/index.html',dict)

