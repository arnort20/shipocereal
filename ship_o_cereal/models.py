from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField

'''class Users(models.Model):
     userId = models.BigAutoField(primary_key=True)
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     realName = models.CharField(max_length=500)
     email = models.CharField(max_length=500)
     password = models.CharField(max_length=255)
     banned = models.BooleanField()'''


class DefaultFilters(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    notVegan = models.BooleanField(default=False)
    gluten = models.BooleanField(default=False)
    wheat = models.BooleanField(default=False)
    barley = models.BooleanField(default=False)
    peanut = models.BooleanField(default=False)
    soy = models.BooleanField(default=False)
    maize = models.BooleanField(default=False)
    sesame = models.BooleanField(default=False)
    buckwheat = models.BooleanField(default=False)
    rice = models.BooleanField(default=False)
    milk = models.BooleanField(default=False)
    oats = models.BooleanField(default=False)
    egg = models.BooleanField(default=False)
    sulphites = models.BooleanField(default=False)


class ProductTypes(models.Model):
    typeId = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=30)


class Manufacturers(models.Model):
    manId = models.BigAutoField(primary_key=True)
    manufacturer = models.CharField(max_length=100)


class Products(models.Model):
    productId = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    typeId = models.ManyToManyField(ProductTypes)
    manId = models.ManyToManyField(Manufacturers)
    price = models.IntegerField()
    image = models.CharField(max_length=999)
    stock = models.IntegerField()
    isFood = models.BooleanField(null=False)


class Nutrients(models.Model):
    productId = models.OneToOneField(Products, on_delete=models.CASCADE, primary_key=True)
    nutritionLabel = models.CharField(max_length=999, null=True)
    notVegan = models.BooleanField(default=False)
    gluten = models.BooleanField(default=False)
    wheat = models.BooleanField(default=False)
    barley = models.BooleanField(default=False)
    peanut = models.BooleanField(default=False)
    soy = models.BooleanField(default=False)
    maize = models.BooleanField(default=False)
    sesame = models.BooleanField(default=False)
    buckwheat = models.BooleanField(default=False)
    rice = models.BooleanField(default=False)
    milk = models.BooleanField(default=False)
    oats = models.BooleanField(default=False)
    egg = models.BooleanField(default=False)
    sulphites = models.BooleanField(default=False)



class Creditcards(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    cardId = models.BigAutoField(primary_key=True)
    cardname = models.CharField(max_length=255)
    cardNumber = models.CharField(max_length=16)
    month = models.IntegerField()
    year = models.IntegerField()
    cvc = models.IntegerField()


class Addresses(models.Model):
    addrId = models.BigAutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    apt_num = models.IntegerField(null=True)
    zip = models.IntegerField()
    country = CountryField(null=True)

class Carts(models.Model):
    cartId = models.BigAutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class CartRows(models.Model):
    cartRowId = models.BigAutoField(primary_key=True)
    cartId = models.ForeignKey(Carts, on_delete=models.CASCADE)
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.IntegerField()


class CartFolio(models.Model):
    folioId = models.BigAutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.IntegerField()


class Orders(models.Model):
    cartId = models.OneToOneField(Carts, on_delete=models.CASCADE, primary_key=True)
    date = models.DateField()
    cardId = models.ForeignKey(Creditcards, on_delete=models.SET_NULL, null=True)
    addrId = models.ForeignKey(Addresses, on_delete=models.SET_NULL, null=True)


class Comments(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    stars = models.IntegerField()
    review = models.CharField(max_length=500)
