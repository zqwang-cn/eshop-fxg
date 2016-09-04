#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Brand(models.Model):
    name=models.CharField(max_length=50)
    country=models.CharField(max_length=30)
    desc=models.TextField()
    def __unicode__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    def __unicode__(self):
        return self.name

class Item(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    desc=models.TextField()
    brand=models.ForeignKey(Brand)
    category=models.ForeignKey(Category)
    status=models.CharField(max_length=10,default='NORMAL',choices=(
        ('NORMAL','正常'),
        ('SALE','促销'),
        ('SOLDOUT','已卖完'),
        ('HOT','热卖'),
    ))
    def __unicode__(self):
        return self.name

class Image(models.Model):
    item=models.ForeignKey(Item)
    img=models.ImageField(upload_to='images/')
    def __unicode__(self):
        return self.item.name
