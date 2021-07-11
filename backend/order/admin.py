from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','client', 'mobile', 'address', 'status', 'total_price', 'paid', 'ordered_date']
    list_editable = ['status']
    list_filter = ['ordered_date']
    list_display_links = []
    fields = []  
    readonly_fields =['client', 'mobile', 'address', 'total_price', 'paid']

    def has_delete_permission(self, request, obj=None):
           return False
