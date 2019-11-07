from django.shortcuts import render

from .forms import FormField

def index(request):
	form_field = FormField()

	dict = {
		'heading':'Home',
		'data_form':form_field,
	}
	return render (request, 'index.html', dict)