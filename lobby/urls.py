from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('detail/<int:queue_id>/', views.detail, name="detail"),
    path('dashboard/<int:queue_id>/', views.dashboard, name="dashboard"),
    path('users-dashboard/', views.users_dashboard, name="user-dash"),
    path('add-user/<int:queue_id>/<int:profile_id>/',views.add_user,name="adduser"),
    path('add-query/<int:queue_id>',views.add_query,name="addquery"),
    path('update-dash/<int:queue_id>',views.update_dash,name="updatedash"),
    path('delete-dash/<int:queue_id>',views.delete_dash,name="deletedash"),
]
