from django.urls import path, re_path

from . import views

urlpatterns = [
	# re_path(r'^khusus/(?<input>[\w-]+)$',views.khusus),
	path('khusus/<str:input>/',views.khusus , name='khusus'),
	path('category/',views.categoryPost , name='category'),
	path('single/',views.singlePost , name ='single'),
	path('',views.index , name='index'),

]