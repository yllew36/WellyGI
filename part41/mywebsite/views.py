from django.shortcuts import render
from django.views import View



def index(request):
	dict = {
		'heading':'Selamat Datang'
	}

	if request.method == 'POST':
		dict['heading'] = 'POST function based view'

	return render(request,'index.html',dict)

class IndexClassViews(View):

	template_name = 'index.html'
	dict = {}
	# override method get darii parent class View

	def get(self,request):
		self.dict['heading'] = 'Get class based view'
		return render (request, self.template_name,self.dict)

	def post(self,request):
		self.dict['heading'] = 'POST class based view'
		return render (request,self.template_name, self.dict)