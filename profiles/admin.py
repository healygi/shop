"""imports for admin page"""

from django.contrib import admin
from .models import UserProfile, WishListItem


class UserProfileAdmin(admin.ModelAdmin):
    """Allows admin to manage profiles via the admin panel"""
    list_display = (
     'user',
     'default_phone_number',
     'default_street_address1',
     'default_street_address2',
     'default_county',
     'default_postcode',
     'default_country',
    )


class WishListItemAdmin(admin.ModelAdmin):
    """Allows admin to manage wishlist items via the admin panel"""
    readonly_fields = (
        'user',
        'product',
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(WishListItem, WishListItemAdmin)
