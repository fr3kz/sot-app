from django.urls import path 
from . import views
from django.views.decorators.csrf import csrf_exempt


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
    path('profile/',views.profile,name="profile"),
    path('profile/<int:profile_id>/',views.profile_detail,name="profiledetail"),
    path('rate/<int:queue_id>',views.rate,name="rate"),
    path('rate-plus/<int:user_id>/<int:queue_id>',views.rep_plus,name="repplus"),
    path('rate-down/<int:user_id>/<int:queue_id>',views.rep_downvote,name="repdown"),
    path('send-invite/<int:invitator_id>/<int:invited_id>',views.send_invite,name="sendinvite"),
    path('accept-invite/<int:invitator_id>/<int:invited_id>',views.accept_invite,name="acceptinvite"),
    path('reject-invite/<int:invitator_id>/<int:invited_id>',views.reject_invite,name="rejectinvite"),
    path('delete-friend/<int:friend_id>',views.delete_friend,name="deletefriend"),
    path('options/<int:queue_id>',views.show_options,name="options"),
    path('add-user-invite/<int:queue_id>/<int:profile_id>/', views.add_userinvite,name="adduserinvite"),
    path('show-userinvites/<int:profile_id>/',views.show_userinvites,name="showuserinvites"),
    path('accept-invi/<int:ivitation_id>/', views.accept_userinvitation,name="acceptuserinvite"),
    path('delete-invi/<int:ivitation_id>/', views.delete_userinvitation,name="deleteuserinvite"),
    path('deletenotification/<int:notification_id>/', views.delete_notification, name="deletenotification"),
    path('categories/', views.categories_list, name="categories"),
    path('category_detail/<int:category_id>/', views.category_detail, name="categorydetail"),
    #api
    path('api/categories/', views.CategoriesList.as_view(), name="categories_list"),
    path('api/queues/', views.QueuesList.as_view(), name="queues_list"),
]
  
