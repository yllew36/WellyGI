from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('contact/', include(('contact.urls', 'contact'))),
    path('admin/', admin.site.urls),

]
