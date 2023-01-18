from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_view, name='create_user'),
    path('retrieve/', views.retrieve_view, name='list_view'),
    path('<int:id>/', views.detail_view, name='detail_view'),
    path('update/', views.update_view, name='update_view'),
    path('delete/', views.delete_view, name='delete_view'),
]
