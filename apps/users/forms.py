# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.core.exceptions import ValidationError


class UserRegistrationForm(DjangoUserCreationForm):
    """
    사용자 회원가입 폼
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "이메일"
        })
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "사용자명"
            }),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields["password1"].widget = forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "비밀번호"
        })
        self.fields["password2"].widget = forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "비밀번호 확인"
        })

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError(u"이미 존재하는 이메일입니다.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError(u"이미 존재하는 사용자명입니다.")
        return username


class UserLoginForm(forms.Form):
    """
    사용자 로그인 폼
    """
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "사용자명 또는 이메일"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "비밀번호"
        })
    )
