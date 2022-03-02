from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    img=models.ImageField(upload_to='categoryimg',blank=True)

    class Meta:
        ordering=['name']
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True,blank=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='productimg', blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    stock=models.IntegerField(blank=True)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['name']
        verbose_name = 'producted'
        verbose_name_plural = 'productss'

    def __str__(self):
        return self.name


class Customer(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=250,blank=True)
    email_id=models.CharField(max_length=250,unique=True,blank=True)
    phone=models.IntegerField(blank=True)
    address=models.CharField(max_length=250,blank=True)
    product=models.ManyToManyField(Product,blank=True,null=True)

    def __str__(self):
        return self.name