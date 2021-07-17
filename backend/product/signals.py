from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Book
from order.models import Order

@receiver(post_save, sender=Book)
def increase_number_of_books(sender, instance, created, **kwargs):
   ''' Increase author's books by one when create new book'''
   if created:
       instance.author.number_of_books +=1
       instance.author.save()

@receiver(post_delete, sender=Book)
def decrease_number_of_books(sender, instance, **kwargs):
   ''' Decrease author's books by one when delete book'''
   instance.author.number_of_books -=1
   instance.author.save()

@receiver(post_save, sender=Order)
def increase_number_of_books(sender, instance, created, **kwargs):
   '''
       Decrease the quantity of book in stock when user create order & clear
       shopcart item 
   '''
   if created:
       for item in instance.client.shopcart_item.all():
              item.book.stock_amount -= item.quantity
              item.book.save()
              if item.book.stock_amount == 0:
                     item.book.available = False
              item.book.save()
              #item.delete()