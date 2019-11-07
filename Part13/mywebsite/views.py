from django.shortcuts import render


def index(request):
	dict = {
		'title':'Kelas Terbuka',
		'heading':'Selamat Datang',
		'subheading':'di index',
	}
	return render(request,'index.html', dict)
