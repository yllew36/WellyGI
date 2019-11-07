from django.shortcuts import render, redirect

# Create your views here.

from .models import Instagram
from .forms import InstagramForm

def delete(request,delete_id):
	Instagram.objects.filter(id=delete_id).delete()
	return redirect('sosmed:list')

def update(request,update_id):
	akun_update = Instagram.objects.get(id=update_id)
	
	data = {
		'nama_depan'	: akun_update.nama_depan,
		'nama_belakang'	: akun_update.nama_belakang,
		'username'		: akun_update.username,
	}

	akun_form = InstagramForm(request.POST or None, initial = data, instance = akun_update)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('sosmed:list')

	dict = {
		'page_title':'Update Akun',
		'akun_form':akun_form,
	}

	return render (request,'sosmed/create.html',dict)


	return redirect('sosmed:list')

def create (request):
	akun_form = InstagramForm(request.POST or None)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('sosmed:list')

	dict = {
		'page_title':'Tambah Akun',
		'akun_form':akun_form,
	}

	return render (request,'sosmed/create.html',dict)

def list(request):
	semua_akun = Instagram.objects.all()

	dict = {
		'page_title':'Sosial Media',
		'semua_akun':semua_akun,
	}
	return render (request,'sosmed/list.html',dict)