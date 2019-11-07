from django.contrib import admin
from django.urls import path

from django.views.generic.base import TemplateView, RedirectView

from . import views

urlpatterns = [
	path('home/',views.HomeView.as_view(),name='home_view'),
	path('rumah', RedirectView.as_view(pattern_name='index'),name='rumah'),
	path('home', RedirectView.as_view(url='/'),name='home'),
	path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('admin/', admin.site.urls),
    path('home/<str:user>/', views.HomeRedirectView.as_view(),name='home_redirect'),
    path('<str:user>', views.HomeUserView.as_view(),name='user'),
]
