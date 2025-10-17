# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Memo(models.Model):
    """
    메모 모델
    사용자가 작성한 메모를 저장합니다.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="memos")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "메모"
        verbose_name_plural = "메모"
        ordering = ["-created_at"]

    def __str__(self):
        return u"{}".format(self.title)

    def get_absolute_url(self):
        return reverse("memos:memo_detail", kwargs={"pk": self.pk})
