from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
	path('blog/',include(('blog.urls', 'blog'))),
	path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
