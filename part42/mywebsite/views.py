from django.shortcuts import render
from django.views.generic.base import TemplateView



# inheritance dari TemplateResponseMixin
# ContextMixin
# View
class IndexView(TemplateView):
	pass

class ContextView(TemplateView):
	template_name	=	'context.html'

	def get_context_data(self):
		dict = {
			'judul':'Home Context',
			'penulis':'Rahasia',
		}
		return dict

class ParameterView(TemplateView):
	template_name = 'parameter.html'

	def get_context_data(self, *args, **kwargs):
		dict = super().get_context_data(**kwargs)

		# dict = kwargs
		print(dict)
		dict ['judul'] = 'Home Parameter'
		dict ['penulis'] = 'RahasiaParam'

		return dict