from django.urls import path
from django.views.generic import ListView,DetailView, FormView


from . import views 
from .models import ArtikelModel
from .forms import ArtikelForm

urlpatterns = [
	path('delete/<str:pk>/',views.ArtikelDeleteView.as_view(),name='delete'),
	path('update2/<str:pk>/',views.ArtikelUpdateView2.as_view(),name='update2'),
	path('update1/<str:pk>/',views.ArtikelUpdateView1.as_view(),name='update1'),
	path('create/',views.ArtikelCreateView2.as_view(),name='create'),
	# path('create/',views.ArtikelCreateView1.as_view(),name='create'),
	# path('create/',views.ArtikelFormView.as_view(),name='create'),
	# path('create/',FormView.as_view(form_class=ArtikelForm,template_name='blog/create.html'),name='create'),
	path('<str:penulis>/<int:page>/',views.ArtikelListView.as_view(),name='list'),
	path('<str:penulis>/',views.ArtikelListView.as_view(),name='list'),
	path('detail/<str:slug>/',views.ArtikelDetailView.as_view(),name='detail'),
	# path('detail/<str:slug>/',DetailView.as_view(model=ArtikelModel),name='detail'),
	# path('', ListView.as_view(model=ArtikelModel), name='list'),
]