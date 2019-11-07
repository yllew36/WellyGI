from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('',include(('blog.urls', 'blog'))),
    path('admin/', admin.site.urls),
]
