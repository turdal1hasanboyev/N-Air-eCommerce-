from django.contrib import admin

from .models import Category, Product, Tag, Review, Banner


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', "updated_at", "is_active") ### adminkada ko'rinadigan ma'lumotlar
    prepopulated_fields = {'slug': ('name',)} ## avtomatik slug yozish uchun


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', "updated_at", "is_active")
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'category',
        'author',
        'price_type',
        'price',
        'percentage',
        'views_count',
        #'discount', ### ishlamadi bu field
        'created_at',
        'updated_at',
        'is_active',
    )

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'rating', 'created_at', 'updated_at', 'is_active')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'name_2',
        'created_at',
        'updated_at',
        'is_active',
    )
