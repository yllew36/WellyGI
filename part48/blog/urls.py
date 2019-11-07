from django.urls import path
from django.views.generic import ListView,DetailView, FormView


from . import views 
from .models import ArtikelModel
from .forms import ArtikelForm

urlpatterns = [
	path('create/',views.ArtikelFormView.as_view(),name='create'),
	# path('create/',FormView.as_view(form_class=ArtikelForm,template_name='blog/create.html'),name='create'),
	path('<str:penulis>/<int:page>/',views.ArtikelListView.as_view(),name='list'),
	path('<str:penulis>/',views.ArtikelListView.as_view(),name='list'),
	path('detail/<str:slug>/',views.ArtikelDetailView.as_view(),name='detail'),
	# path('detail/<str:slug>/',DetailView.as_view(model=ArtikelModel),name='detail'),
	# path('', ListView.as_view(model=ArtikelModel), name='list'),
]