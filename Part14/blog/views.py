from django.shortcuts import render

def index(request):
	dict = {
	'title':'Blog',
	'heading':'Blog',
	'subheading':'Jurnal Kelas Terbuka',
	}
	return render(request,'blog/index.html', dict)