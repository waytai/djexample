#########################################################################
#-*- coding:utf-8 -*-
# File Name: models.py
#########################################################################
#!/bin/python
#_*_coding:utf-8_*_
from django.db import models
# Create your models here.

class Colors(models.Model):
    colors=models.CharField(max_length=10) #蓝色
    def __str__(self):
        return self.colors

class Ball(models.Model):
    color=models.OneToOneField("Colors")  #与颜色表为一对一，颜色表为母表
    description=models.CharField(max_length=10) #描述
    def __str__(self):
        return self.description

class Clothes(models.Model):
    color=models.ForeignKey("Colors")   #与颜色表为外键，颜色表为母表
    description=models.CharField(max_length=10) #描述
    def __str__(self):
        return self.description

class Child(models.Model):
    name=models.CharField(max_length=10)   #姓名  
    favor=models.ManyToManyField('Colors')    #与颜色表为多对多


class Publication(models.Model):
    title = models.CharField(max_length=30)
    # On Python 3: def __str__(self):  
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    # On Python 3: def __str__(self):  
    def __unicode__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
