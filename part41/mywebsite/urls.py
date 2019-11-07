from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('class/',views.IndexClassViews.as_view(template_name='index.html'), name='home-class'),
	path('class2/',views.IndexClassViews.as_view(template_name='index2.html'), name='home-class2'),
    path('admin/', admin.site.urls),
]
