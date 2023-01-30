from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin class for the Review model.
    """
    list_display = (
        'user',
        'product',
        'product_rating',
        'title',
        'user_review',
        'date_created',
    )
    list_filter = (
        'user',
        'product',
        'product_rating',
        'date_created',
    )
    search_fields = [
        'user__username',
        'title',
        'product__name'
    ]
    list_per_page = 15


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
