from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand/')

    def __str__(self):
        return self.name


class Slide(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='slide/')
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Digikala_Services(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='service/')
    url = models.URLField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Guarantees(models.Model):
    name = models.CharField()
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(24)])

    def __str__(self):
        return self.name


class OfferPack(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='offer/')
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    brands = models.ManyToManyField(Brand, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    offer_status = models.BooleanField(default=False)
    offer_price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='product/')
    buy_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class News(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news/')
    url = models.URLField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
