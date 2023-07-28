from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('users',views.list_users, name="list-user"),
    path('new_user', views.register_user, name="new-user"),
    path('users/<int:id>/', views.user_detail, name="user-detail"),
]
