from django.urls import path
from . import views

urlpatterns = [
       path('signup/', views.SignUpView().as_view(), name ='signup'),
       path('update/', views.UpdateUserView.as_view(), name='update'),
]