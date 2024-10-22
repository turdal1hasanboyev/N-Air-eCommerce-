from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', "updated_at")
    prepopulated_fields = {'slug': ('name',)} ## avtomatik slug yozish uchun
