from django.shortcuts import render
from django.views.generic import ListView

from .models import ArtikelModel


class ArtikelListView(ListView):
    model = ArtikelModel
    ordering = ['id']
    extra_context = {
        'page_title': 'Blog Listtt'
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


def index(request):

    dict = {
        'page_title': 'Blog',

    }
    return render(request, 'blog/index.html', dict)
