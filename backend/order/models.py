from django.db import models
from user.models import User
from django.utils.translation import ugettext_lazy as _

# prodouct -> add prodouct to shopcart -> make order -> save shopcart as bought item -> clear shopcart 

class Order(models.Model):
       PENDING = 'PENDING'
       IN_DELIVERY = 'In_delivery'
       DELIVERED = 'Delivery'

       order_status = [
       (PENDING, _('Pending')),
       (IN_DELIVERY, _('In_delivery')),
       (DELIVERED, _('Delivery')),
       ]
       
       client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_client', blank=True, null=True)
       mobile = models.CharField(_('mobile'), max_length=125, blank=True, null=True, help_text=_('Contact phone number'))
       ordered_date = models.DateTimeField(auto_now_add=True)
       address = models.CharField(_('address'), max_length=125)
       paid = models.BooleanField(default=False)
       status = models.CharField(max_length=125, choices=order_status, default=PENDING)
       total_price = models.FloatField(blank=True, null=True)

       def save(self, *args, **kwargs):
              self.total_price = self.client.total_cart_price
              super().save(*args, **kwargs)

       def __str__(self):
              return f"Order Price: {self.total_price}"

       @property
       def order_product(self):
              return list(self.client.shopcart_item.all())