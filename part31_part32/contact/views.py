from django.shortcuts import render

# Create your views here.

from .forms import ContactForm

def index(request):
	contact_form = ContactForm
	dict = {
		'heading':'Contact',
		'data_form':contact_form,
	}
	return render(request, 'index.html', dict)