from django.contrib import admin

# Register your models here.
from app.models import Product, Contact

admin.site.register(Product)
admin.site.register(Contact)