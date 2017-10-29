# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib import admin

# Create your models here.

class Category(models.Model):
    catName = models.CharField(max_length=128, unique=True, null=False)
    catSlug = models.SlugField(unique=True, null=False)

    def save(self, *args,**kwargs):
        self.catSlug = slugify(self.catName)
        super(Category, self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.catName

class CategoryAdmin(admin.ModelAdmin):
    list_display=('catName','catSlug')

class Product(models.Model):
    category = models.ForeignKey(Category, null=False)
    prodName = models.CharField(max_length=128, unique=True, null=False)
    prodSlug = models.SlugField(unique=True, null=False)
    image = models.ImageField(upload_to='static/images/products', blank=True, null= False)
    description = models.CharField(max_length=256, null=False)
    price = models.DecimalField(null=False, decimal_places=2, max_digits=5)
    stock = models.IntegerField(null=False, default=1)
    availability = models.BooleanField(null=False, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.prodSlug = slugify(self.prodName)
        super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.prodName

class ProductAdmin(admin.ModelAdmin):
    list_display=('prodName','prodSlug','price','stock','availability','created','updated')