from django.shortcuts import render

# Create your views here.

#import form
from .forms import ContactForm

def index(request):

	contact_form = ContactForm()

	dict = {
		'heading':'Contact Form',
		'form':contact_form,



	}

	if request.method == 'POST':
		print("ini adalah method POST")
		dict['nama'] = request.POST['nama']
		dict['alamat'] = request.POST['alamat']

	else :
		print("ini adalah method GET")
	return render (request,'contact/index.html', dict)