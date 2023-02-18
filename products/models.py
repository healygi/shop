from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

from .products_choices import RATING_CHOICES


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)  # noqa: E501
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # noqa: E501
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    The Review model class, creating an instance of a review
    """

    class Meta:
        """
        Meta class enables ordering by id
        """

        ordering = ['id']

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    title = models.CharField(verbose_name=_('Review Title'), max_length=25, null=False, blank=False)  # noqa: E501
    user_review = models.TextField(verbose_name=_('User Review'), max_length=250, null=False, blank=False)  # noqa: E501
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns review title field as a string
        Args:
            self (object)
        Returns:
            The review title
        """
        return f'{self.title}'
