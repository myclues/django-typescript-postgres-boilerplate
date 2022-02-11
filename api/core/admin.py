from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserForms

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    add_form = UserForms.UserCreationForm
    form = UserForms.UserChangeForm

    search_fields = ['username', 'email', 'first_name', 'last_name',]
    list_display = ['username', 'email', 'is_admin', 'is_staff', 'is_active',]
    list_filter = ('is_admin', 'is_staff', 'is_active')

    readonly_fields = ('created', 'updated', 'last_login')

    ordering = ('username', 'email', )

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password', ('first_name', 'last_name'), )
        }),
        ('Permissions', {
            'fields': ('is_admin', 'is_staff', 'is_active')
        }),
        ('Time', {
            'fields': ('last_login', 'created', 'updated')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)
        }),
    )