from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES=(
    ('YG', 'Yogort'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
)
STATE_CHOICES=(
    ('Koshi Pradesh', 'Koshi Pradesh'), 
    ('Madhesh Pradesh', 'Madhesh Pradesh'),
    ('Bagmati Pradesh', 'Bagmati Pradesh'),
    ('Gandaki Pradesh', 'Gandaki Pradesh'),
    ('Lumbini Pradesh', 'Lumbini Pradesh'),
    ('Karnali Pradesh', 'Karnali Pradesh'),
    ('Sudur Pashchim Pradesh', 'Sudur Pashchim Pradesh')

)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image=models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality= models.CharField(max_length=200)
    city =models.CharField(max_length=50)
    mobile =models.IntegerField(default=0)
    # zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def _str_(self):
        return self.name
    

# class User(models.Model):
#     username=models.CharField(max_length=30)
#     email=models.EmailField()
#     password1=models.CharField(max_length=10)
#     password2=models.CharField(max_length=10)

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField()
    message =models.TextField()
    def _str_(self):
        return self.name
    