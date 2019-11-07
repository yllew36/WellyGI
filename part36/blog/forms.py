from django import forms

# import model dari models.py

from .models import Post

# class PostForm(forms.Form):
# 	judul		= forms.CharField(max_length=100)
# 	body		= forms.CharField(widget=forms.Textarea)
# 	category	= forms.CharField(max_length=100)


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'author',
			'judul',
			'body',
			'category',
		]