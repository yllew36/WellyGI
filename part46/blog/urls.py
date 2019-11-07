from django.urls import path
from django.views.generic import ListView


from . import views 
from .models import ArtikelModel


urlpatterns = [
	path('<str:penulis>/<int:page>/',views.ArtikelListView.as_view(),name='list'),
	# path('', ListView.as_view(model=ArtikelModel), name='list'),
]