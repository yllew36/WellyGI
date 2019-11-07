from django.shortcuts import render

def index(request):
	dict = {
		'heading':'Home Form',
	}
	if request.method == 'POST':
		print("ini adalah method POST")
		dict ['nama'] = request.POST['nama']
		dict ['alamat'] = request.POST['alamat']
	else :
		print("ini adalah method Get")

	return render(request, 'index.html', dict)