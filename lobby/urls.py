from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add-user/',views.add_user,name="adduser"),
    path('remove-user/',views.remove_user,name="removeuser"),
]
