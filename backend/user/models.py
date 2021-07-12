from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Sum, F, FloatField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib import admin

def upload_avatar(instance, filename):
    return 'users/{0}/{1}'.format(instance.id, filename)


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
            
        user = self.model(
            email=self.normalize_email(email),
             **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
       
        user = self.create_user(
            email,
            password,
            **extra_fields
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), max_length=125, blank=True, null=True, unique=True)
    mobile = PhoneNumberField(_('mobile'), max_length=125, unique=True, blank=True, null=True, help_text=_('Contact phone number'))                                
    full_name = models.CharField(_('full_name'), max_length=225, blank=True, null=True)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_active = models.BooleanField(_('is_active'), default=True)
    avatar = models.FileField(blank=True, null=True, upload_to=upload_avatar)
    address = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('User')

    def __str__(self):
        return self.email

    @property    
    def total_cart_price(self):
        return self.shopcart_item.aggregate(total=Sum(F('book__price') * F('quantity') , output_field=FloatField()) )['total']
    