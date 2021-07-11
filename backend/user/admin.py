from .models import User 
from django.contrib import admin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['email', 'mobile','full_name', 'address']
    readonly_fields = ['mobile','full_name', 'address']
    list_filter = []
    list_editable = []
    ordering = []

    fieldsets = (
        (None, {'fields': ( 
            'email', 'mobile','address', 'full_name',
            ('is_active','is_superuser','is_staff'),
            
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password',('is_superuser', 'is_staff') ), 
        }),
    )

admin.site.unregister(Group)