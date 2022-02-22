from django.db import models

# Create your models here.

class destination(models.Model):
    # id:int
    # name:str
    # img:str
    # des:str
    # price:int
    # off:
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    des = models.TextField()
    price = models.IntegerField()   
    off = models.BooleanField(default=False)
    

class news(models.Model):
    date = models.IntegerField()
    month =models.IntegerField()
    head = models.CharField(max_length=100)
    des = models.CharField(max_length=100)
    img = models.ImageField(upload_to='photos')
