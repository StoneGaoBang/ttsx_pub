# coding=utf-8
from django.db import models


class UserInfo(models.Model):
    uaccounts = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    umail = models.CharField(max_length=30)
    uaddress = models.CharField(max_length=100)
    uname = models.CharField(max_length=10)
    uphone = models.CharField(max_length=11)
    ucode = models.CharField(max_length=6)
