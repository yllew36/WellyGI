from django import forms

from .models import ArtikelModel

class ArtikelForm(forms.ModelForm):
	class Meta:
		model = ArtikelModel
		fields = [
			'judul',
			'isi',
			'penulis',
		]