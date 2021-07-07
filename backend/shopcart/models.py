from django.db import models
from user.models import User
from product.models import Book
#from order.models import Order, BoughtItem
from django.db.models.signals import post_save
from django.dispatch import receiver

class ShopCart(models.Model):
   client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopcart_item', blank=True, null=True)
   book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='shopcart_books')
   quantity = models.PositiveSmallIntegerField(default=1)

   @property
   def item_cost(self):
      return self.quantity * self.book.price

   def __str__(self):
      return f"product id: {self.book_id}, Price: {self.item_cost} EGP, quantity :{self.quantity}"
