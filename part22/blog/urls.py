from django.urls import path
from . import views

urlpatterns =[
	path('',views.index),
	path('jurnal/',views.jurnal),
	path('berita/',views.berita),
	path('gosip/',views.gosip),
]