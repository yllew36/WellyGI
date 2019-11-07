from django.urls import path

from . import views

urlpatterns = [
	path('delete/<int:delete_id>/',views.SosmedDeleteView.as_view(),name='delete'),
	path('update/<int:update_id>/',views.SosmedFormView.as_view(mode='update'),name='update'),
	path('create/',views.SosmedFormView.as_view(), name='create'),
	path('',views.SosmedListView.as_view(), name='list'),
]