from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
	path('artikel/', include(('artikel.urls','artikel'))),
	path('',TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
]
