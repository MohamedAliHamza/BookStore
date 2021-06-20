from django.urls import path
from . import views

urlpatterns = [
       path('update_user/', views.UserUpdateView.as_view()),
]