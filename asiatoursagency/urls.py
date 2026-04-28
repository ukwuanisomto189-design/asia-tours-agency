from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_tour, name='add_tour'),
    path('edit/<int:tour_id>/', views.edit_tour, name='edit_tour'),
    path('delete/<int:tour_id>/', views.delete_tour, name='delete_tour'),
]