# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from shop.models import Category, Product, CategoryAdmin, ProductAdmin
from django.contrib import admin

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

# Register your models here.
