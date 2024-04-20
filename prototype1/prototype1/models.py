
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# from .models import CustomUser
from django import forms


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Add more fields as needed

    # Specify unique related_name values for groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.email


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    # Add more fields as needed

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', related_name='carts')

    def __str__(self):
        return f'Cart for {self.user.username}'
