from django.urls import path


from .views import (
	ArtikelListView, 
	ArtikelDetailView, 
	ArtikelKategoriListView,
	ArtikelCreateView,
	ArtikelManageView,
	ArtikelDeleteView,
	ArtikelUpdateView,
	)


urlpatterns = [
	path('manage/edit/<int:pk>',ArtikelUpdateView.as_view(),name='edit'),
	path('manage/delete/<int:pk>', ArtikelDeleteView.as_view(), name='delete'),
	path('manage/', ArtikelManageView.as_view(), name='manage'),
	path('tambah/',ArtikelCreateView.as_view(),name='tambah'),
	path('kategori/<str:kategori>/<int:page>/',ArtikelKategoriListView.as_view(),name='kategori'),
	path('detail/<str:slug>/',ArtikelDetailView.as_view(),name='detail'),
	path('<int:page>/',ArtikelListView.as_view(),name='list'),
]