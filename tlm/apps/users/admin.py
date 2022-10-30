from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from tlm.apps.users.models import User


class CustomUserAdmin(UserAdmin):
    """
    Admin configuration for the custom User model.
    """

    list_display = ('username', 'email', 'full_name', 'first_name', 'last_name', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'full_name', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'password1', 'password2')}
         ),
    )

    search_fields = ['username', 'email', 'full_name']


admin.site.register(User, CustomUserAdmin)
