from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategorytAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slugs": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "stock","Category", "created_at")
    search_fields = ("name",)
    list_filter = ("Category",)

