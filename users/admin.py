from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreateForm
from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ('Campos personalizados', {'fields': ('bio',)}),
    )
