from django.urls import path, re_path

from . import views

urlpatterns = [
	path('',views.index),
	re_path(r'^post/(?P<inputSlug>[\w-]+)/$', views.detailPost),
	re_path(r'^category/(?P<dataCategory>[\w-]+)/$', views.categoryPost),

]