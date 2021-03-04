from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Manager
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = Manager
    list_display = ['pk','email','first_name','last_name']

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email','first_name','last_name')})
    )
    fieldsets = UserAdmin.fieldsets

admin.site.register(Manager, CustomUserAdmin)
