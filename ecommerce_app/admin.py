from django.contrib import admin
from . models import Product, Customer, Contact
# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'discounted_price', 'category', 'product_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'locality','mobile', 'city', 'state']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'email','message']