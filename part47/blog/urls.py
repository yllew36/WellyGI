from django.urls import path
from django.views.generic import ListView,DetailView


from . import views 
from .models import ArtikelModel


urlpatterns = [
	path('<str:penulis>/<int:page>/',views.ArtikelListView.as_view(),name='list'),
	path('<str:penulis>/',views.ArtikelListView.as_view(),name='list'),
	path('detail/<str:slug>/',views.ArtikelDetailView.as_view(),name='detail'),
	# path('detail/<str:slug>/',DetailView.as_view(model=ArtikelModel),name='detail'),
	# path('', ListView.as_view(model=ArtikelModel), name='list'),
]