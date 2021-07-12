from django.urls import path
from . import views

urlpatterns = [
       path('signup/', views.SignUpView().as_view(), name ='signup'),
       path('update_user/', views.UserUpdateView.as_view()),
]