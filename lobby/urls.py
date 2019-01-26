from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('detail/<int:queue_id>/', views.detail, name="detail"),
    path('dashboard/<int:queue_id>/', views.dashboard, name="dashboard"),
    path('users-dashboard/', views.users_dashboard, name="user-dash"),
    path('add-user/<int:queue_id>/<int:profile_id>/',views.add_user,name="adduser")
]
