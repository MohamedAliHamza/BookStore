from django.urls import path
from . import views

urlpatterns = [
       path('shopcart/', views.ShopCartView.as_view(), name='shopcart')       

]