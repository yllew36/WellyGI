from django.urls import path

from . import views

urlpatterns = [
	path('delete/<int:delete_id>/',views.delete,name='delete'),
	path('create/',views.create, name='create'),
	path('',views.list, name='list'),
]