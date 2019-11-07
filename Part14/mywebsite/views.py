from django.shortcuts import render


def index(request):
	dict = {
		'title':'Kelas Terbuka',
		'heading':'Selamat Datang',
		'subheading':'Halaman Muka Website Kami',
	}
	return render(request,'index.html', dict)
