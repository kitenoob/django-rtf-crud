from django.urls import path
from api import views

urlpatterns = [
    #path('users', views.UserList.as_view()),
    path('users', views.UserList),
    path('objects', views.ObjectList),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('object/<int:pk>/', views.ObjectDetail.as_view()),
]