# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    사용자 프로필 모델
    Django 내장 User 모델을 확장합니다.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "사용자 프로필"
        verbose_name_plural = "사용자 프로필"

    def __str__(self):
        return u"{}의 프로필".format(self.user.username)
