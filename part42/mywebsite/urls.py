from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
	path('parameter/<int:parameter1>/<int:parameter2>',views.ParameterView.as_view()),
	path('context/', views.ContextView.as_view()),
	path('default/',TemplateView.as_view(template_name='default.html'),name='default'),
	path('', views.IndexView.as_view(template_name='index.html'),name='index'),
    path('admin/', admin.site.urls),
]

'''
1. membuat class view di views.py, tapi menggunakan templatenya di url
2. jika halaman kita statis, tidak ada perubahan apapun,
maka kita lakukan templateview langsung pada urls.py
3.  membuat views dengan context saja, kita menggunakan class
templateview di views.py
4. kita memasukan parameter kedalam template, dengan menggunakan regex

'''
