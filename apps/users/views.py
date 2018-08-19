from django.shortcuts import render

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import authentication
from random import choice

from shop.settings import APIKEY
from utils.yunpian import YunPian
from .models import VerifyCode

User = get_user_model()
# Create your views here.

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None



class SmsCodeViewSet():
