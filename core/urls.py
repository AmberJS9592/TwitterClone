from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:core_id>/', views.delete, name='delete'),
    path('edit/<int:core_id>/', views.edit, name='edit'),
    path('like/<int:core_id>/', views.LikeView, name='like_post')
]