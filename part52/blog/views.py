from django.views.generic import TemplateView

from artikel.views import ArtikelPerKategori

class BlogHomeView(TemplateView, ArtikelPerKategori):
	template_name = "index.html"

	def get_context_data(self):
		queryset = self.get_latest_artikel_each_kategori()
		context = {
			'latest_artikel_list':queryset
		}
		return context

