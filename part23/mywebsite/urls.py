from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    re_path(r'^(?P<input>[0-9]+)/$', views.angka),
    re_path(r'^(?P<tahun>[0-9]{4})/(?P<bulan>[0-9]{2})/(?P<tanggal>[0-9]{2})/$', views.tanggal),
    re_path(r'^(?P<page>[\w_-]+)/$',views.link),
]
