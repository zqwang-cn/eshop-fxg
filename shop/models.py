#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

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
    super=models.ForeignKey('self',null=True,blank=True,default=None)
    def __unicode__(self):
        return self.name

class Item(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    oldprice=models.DecimalField(max_digits=10,decimal_places=2,default=99.8)
    desc=models.TextField()
    richdesc=HTMLField()
    brand=models.ForeignKey(Brand)
    category=models.ForeignKey(Category)
    thumb=models.ImageField(upload_to='thumbs/')
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

class CartItem(models.Model):
    user=models.ForeignKey(User)
    item=models.ForeignKey(Item)
    num=models.IntegerField()
