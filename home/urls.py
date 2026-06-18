from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list, name='character_list'),
    path('characters/<int:pk>/', views.character_detail, name='character_detail'),
    path('api/characters/', views.character_api, name='character_api'),
    path('api/characters/<int:pk>/', views.character_api_detail, name='character_api_detail'),
]
