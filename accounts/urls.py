from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),

    #api
    path('api/login',views.Login.as_view()),
    path('api/register',views.Register.as_view()),
    #path('api/logout/<int:id>', views.Logout.as_view())
]
