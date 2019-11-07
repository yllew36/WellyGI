from django.http import HttpResponse

# Create your views here.


from .models import Post

def index(request):
	

	return HttpResponse("testing")


def categoryPost(request, categoryInput):
	posts = Post.objects.filter(category=categoryInput)

	return HttpResponse ("category Post")


def singlePost(request, slugInput):
	posts = Post.objects.get(slug=slugInput)

	judul = "<h1>{}</h1>".format(posts.judul)
	body = "<p>{}</p>".format(posts.body)
	category = "<p>{}</p>".format(posts.category)
	slug = "<p>{}</p>".format(posts.slug)

	return HttpResponse(judul + body + category + slug)

