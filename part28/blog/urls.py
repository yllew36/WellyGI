from django.urls import path, re_path

from . import views

urlpatterns = [
	path('',views.index, name='index'),
	# re_path(r'^post/(?P<inputSlug>[\w-]+)/$', views.detailPost, name='detail'),
	# re_path(r'^category/(?P<dataCategory>[\w-]+)/$', views.categoryPost, name='category'),
	path('post/<slug:inputSlug>/',views.detailPost, name='detail'),
	path('category/<str:dataCategory>/',views.categoryPost, name='category')
]