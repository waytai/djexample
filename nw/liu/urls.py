#########################################################################
#-*- coding:utf-8 -*-
# File Name: urls.py
#########################################################################
#!/bin/python
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^st_cl/', views.stcl),
    url(r'^pb/', views.pbat),
]
