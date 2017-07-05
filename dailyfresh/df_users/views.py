# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import *
from hashlib import sha1


def index(request):
    context = {'title': '首页'}
    return render(request, 'dailyfresh/index.html', context)


def register(request):
    context = {'title': '注册'}
    return render(request, 'dailyfresh/register.html', context)


def register_submit(request):
    uaccounts = request.POST.get('user_name')
    upwd = request.POST.get('pwd')
    umail = request.POST.get('email')

    # 对密码进行sha1加密
    upwd_sha1 = sha1(upwd).hexdigest()

    user = UserInfo()
    user.uaccounts = uaccounts
    user.upwd = upwd_sha1
    user.umail = umail
    user.save()

    return redirect('/login')


def login(request):
    context = {'title': '登录'}
    return render(request, 'dailyfresh/login.html', context)
