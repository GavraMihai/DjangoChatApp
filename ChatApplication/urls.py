from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.index, name="index"),

    path('<str:room>/', views.room, name="room"),
    path('send', views.send, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages"),

    path('loginRoom', views.loginRoom, name="loginRoom"),
    path('uploadImage', views.uploadImage, name="uploadImage")

]
