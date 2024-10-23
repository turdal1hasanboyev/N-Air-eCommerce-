from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ( ### adminkada ko'rinadigan qismi
        "id",
        "get_full_name",
        "get_short_name",
        "first_name",
        "last_name",
        "username",
        "email",
        "phone_number",
        "is_staff",
        "is_active",
        "is_superuser",
        "date_joined",
        "clean",
        "created_at",
        "updated_at",
    )
    