from django.contrib import admin
from .models import User 
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label=_('password'), widget=forms.PasswordInput)
    class Meta:
       model = User
       fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
       model = User
       fields = '__all__'

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'mobile','full_name', 'address')
    list_filter = ()
    list_editable = ()
    ordering = ()
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
            'fields': ('email', 'password','is_superuser' ),
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)