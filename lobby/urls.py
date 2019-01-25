from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('detail/<int:queue_id>/', views.detail, name="detail"),
    path('dashboard/<int:queue_id>/', views.dashboard, name="dashboard"),
    path('add-user/<int:queue_id>/<int:user_id>/',views.add_user,name="adduser"),
    path('remove-user/<int:queue_id>/<int:user_id>/',views.remove_user,name="removeuser"),
]
