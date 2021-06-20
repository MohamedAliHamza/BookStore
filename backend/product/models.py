from django.db import models
from user.models import User
from django.db.models import Sum, F
from django.utils.translation import gettext_lazy as _
from .utilities import product_image, author_image, custom_slugify


class Author(models.Model):
    name = models.CharField(_('name'), max_length=100)  
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    brief = models.TextField(_('brief'))
    number_of_books = models.SmallIntegerField(_('number_of_books'),default=0)
    image = models.FileField(_('image'),upload_to=author_image, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.number_of_books = self.author_book.count()
        self.slug = custom_slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors') 



class Category(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = custom_slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories') 

class Book(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'))
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('added_by'))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('book_author'), related_name='author_book')
    quantity = models.IntegerField()
    image = models.FileField(upload_to=product_image, blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = custom_slugify(self.name)
        #self.added_by = self.request.user 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

## => create signal when add book, number of books of author increased by one 


# class ShopCart(models.Model):
#     client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_shopcart')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='shopcart_product')
#     quantity = models.IntegerField(default=1)

#     def item_cost(self):
#         return self.quantity * self.product.price

#     def __str__(self):
#         return f"client: {self.client} product: {self.product} quantity: {self.quantity} price: {self.item_cost()} "

#     class Meta:
#         verbose_name = _('ShopCart')
#         verbose_name_plural = _('ShopCarts')


# # create order => to order => Order , BoughtItems
# class Order(models.Model):
#     client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user')
#     ordered_date = models.DateTimeField(auto_now_add=True)
#     total_price = models.FloatField(default=0)

#     def __str__(self):
#         return f"client: {self.client} price: {self.total_price}"


# class BoughtItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='boughtitem_product')
#     quantity = models.PositiveIntegerField(default=1)
#     price = models.FloatField(default=0)

#     def item_price(self):
#         return self.price * self.quantity

#     def __str__(self):
#         return f"Order: {self.order} product: {self.product} quantity: {self.quantity} price: {self.item_price()}"
