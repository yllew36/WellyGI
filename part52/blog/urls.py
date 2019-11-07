from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import BlogHomeView

urlpatterns = [
	path('artikel/', include(('artikel.urls','artikel'))),
	path('',BlogHomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
