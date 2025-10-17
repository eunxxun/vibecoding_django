# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from .forms import UserRegistrationForm, UserLoginForm


@require_http_methods(["GET", "POST"])
def register_view(request):
    """
    사용자 회원가입 뷰
    """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("memos:memo_list")
    else:
        form = UserRegistrationForm()

    context = {
        "form": form,
        "page_title": "회원가입"
    }
    return render(request, "users/register.html", context)


@require_http_methods(["GET", "POST"])
def login_view(request):
    """
    사용자 로그인 뷰
    """
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            # username 또는 email로 인증
            user = None
            if "@" in username:
                try:
                    user_obj = User.objects.get(email=username)
                    user = authenticate(username=user_obj.username, password=password)
                except User.DoesNotExist:
                    pass
            else:
                user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("memos:memo_list")
            else:
                form.add_error(None, u"사용자명/이메일 또는 비밀번호가 잘못되었습니다.")
    else:
        form = UserLoginForm()

    context = {
        "form": form,
        "page_title": "로그인"
    }
    return render(request, "users/login.html", context)


@login_required(login_url="users:login")
def logout_view(request):
    """
    사용자 로그아웃 뷰
    """
    logout(request)
    return redirect("users:login")


@login_required(login_url="users:login")
def profile_view(request):
    """
    사용자 프로필 조회 뷰
    """
    context = {
        "page_title": "프로필"
    }
    return render(request, "users/profile.html", context)
