from django.core.exceptions import ValidationError
from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='people/')
    name = models.CharField(max_length=155)
    age = models.PositiveIntegerField(default=20)
    course = models.PositiveIntegerField(default=4)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'


class Contact(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    if phone_number != 13:
        ValidationError('Enter number correctly')
    message = models.TextField()

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
