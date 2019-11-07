from django.urls import path


from .views import (
	ArtikelListView, 
	ArtikelDetailView, 
	ArtikelKategoriListView,
	ArtikelCreateView,
	)


urlpatterns = [
	path('tambah/',ArtikelCreateView.as_view(),name='tambah'),
	path('kategori/<str:kategori>/<int:page>/',ArtikelKategoriListView.as_view(),name='kategori'),
	path('detail/<str:slug>/',ArtikelDetailView.as_view(),name='detail'),
	path('<int:page>/',ArtikelListView.as_view(),name='list'),
]