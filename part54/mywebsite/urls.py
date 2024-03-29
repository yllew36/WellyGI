from django.contrib import admin
from django.urls import path

from .views import index, IndexView, loginView, logoutView

urlpatterns = [
	path('logout/',logoutView, name='logout'),
	path('login/',loginView,name='login'),
	# path('', IndexView.as_view(), name = 'index'),
	path('',index,name='index'),
    path('admin/', admin.site.urls),
]
