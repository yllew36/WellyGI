from django.shortcuts import render

from .models import Post


# Create your views here.
def index(request):
	#query
	posts = Post.objects.all()
	

	dict = {
		'title':'Blog',
		'heading':'Blog di mywebsite',
		'posting':posts,

	}
	return render(request,'blog/index.html',dict)