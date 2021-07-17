from django.db import models
from user.models import User
from django.db.models import Sum, F
from django.utils.translation import gettext_lazy as _
from .utilities import product_image, author_image,category_image, custom_slugify


class Author(models.Model):
    name = models.CharField(_('name'), max_length=100)  
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    brief = models.TextField(_('brief'))
    number_of_books = models.SmallIntegerField(_('number_of_books'),default=0)
    image = models.FileField(_('image'),upload_to=author_image, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        #self.number_of_books = self.author_book.count()
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
    background = models.FileField(upload_to=category_image, blank=True, null=True)

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_books')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('added_by'))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('book_author'), related_name='author_book')
    stock_amount = models.IntegerField()
    available = models.BooleanField(default=True)
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

