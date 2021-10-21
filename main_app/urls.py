from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fishes/', views.fish_index, name='index'),
    path('fish/<int:fish_id>/', views.fish_detail, name='detail'),
    path('fishes/create/', views.FishCreate.as_view(), name='fishes_create'),
    path('fish/<int:pk>/update/', views.FishUpdate.as_view(), name='fish_update'),
    path('fish/<int:pk>/delete/', views.FishDelete.as_view(), name='fish_delete'),
    path('fish/<int:fish_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('fish/<int:fish_id>/add_toy/<int:toy_id>/', views.add_toy, name='add_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]