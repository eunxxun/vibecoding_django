# -*- coding: utf-8 -*-
from django import forms
from .models import Memo


class MemoForm(forms.ModelForm):
    """
    메모 작성/수정 폼
    """
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "제목"
        })
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "내용",
            "rows": 10
        })
    )

    class Meta:
        model = Memo
        fields = ("title", "content")
