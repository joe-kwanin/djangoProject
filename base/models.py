from django.contrib.auth.models import AbstractUser
from django.db import models
from djangoProject.settings import AUTH_USER_MODEL


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=300)
    business_name = models.CharField(max_length=400)
    email = models.EmailField(null=True, blank=True, unique=True)
    atype = models.CharField(null=True, blank=True, max_length=30)
    location = models.CharField(max_length=700)
    contact = models.CharField(max_length=14)
    avatar = models.ImageField(null=True, default='p5.jpg')

    #USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class product(models.Model):
    title = models.CharField(null=True, blank=True, max_length=400)
    desc = models.CharField(null=True, blank=True, max_length=700)
    sku = models.CharField(null=True, blank=True, max_length=20)
    brand = models.CharField(null=True, blank=True, max_length=500)
    price = models.IntegerField(null=True, blank=True, default=0)
    image = models.ImageField(upload_to='product_images')
    cat = models.CharField(null=True, blank=True, max_length=20)
    veterinary = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, default=False)
    score = models.IntegerField(null=True, blank=True, default=0)
    cart_price = models.IntegerField(null=True, blank=True, default=0)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class categories(models.Model):
    name = models.CharField(null=True, blank=True,max_length=300)

    def __str__(self):
        return self.name

class report:
    title = models.CharField(max_length=700)
    body = models.FileField(upload_to=...)
