# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home_view(request):
    """
    홈페이지 뷰
    """
    if request.user.is_authenticated:
        return redirect("memos:memo_list")
    return render(request, "home.html")
