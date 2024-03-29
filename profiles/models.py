from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

from products.models import Product


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)  # noqa: E501
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)  # noqa: E501
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)  # noqa: E501
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)  # noqa: E501
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)  # noqa: E501

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()


class WishListItem(models.Model):
    """
    A model that keeps track of users wish list items.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)
