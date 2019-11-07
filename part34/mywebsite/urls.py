from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('blog/', include(('blog.urls', 'blog'))),
    path('admin/', admin.site.urls),
]
