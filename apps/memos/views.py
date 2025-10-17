# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import Http404
from .models import Memo
from .forms import MemoForm


@login_required(login_url="users:login")
def memo_list_view(request):
    """
    메모 목록 조회 뷰 (사용자별 필터링)
    """
    memos = Memo.objects.filter(user=request.user)
    context = {
        "memos": memos,
        "page_title": "메모 목록"
    }
    return render(request, "memos/memo_list.html", context)


@login_required(login_url="users:login")
def memo_detail_view(request, pk):
    """
    메모 상세 조회 뷰
    """
    memo = get_object_or_404(Memo, pk=pk)
    
    # 소유자 확인
    if memo.user != request.user:
        raise Http404()

    context = {
        "memo": memo,
        "page_title": memo.title
    }
    return render(request, "memos/memo_detail.html", context)


@login_required(login_url="users:login")
@require_http_methods(["GET", "POST"])
def memo_create_view(request):
    """
    메모 작성 뷰
    """
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.user = request.user
            memo.save()
            return redirect("memos:memo_detail", pk=memo.pk)
    else:
        form = MemoForm()

    context = {
        "form": form,
        "page_title": "메모 작성"
    }
    return render(request, "memos/memo_form.html", context)


@login_required(login_url="users:login")
@require_http_methods(["GET", "POST"])
def memo_update_view(request, pk):
    """
    메모 수정 뷰
    """
    memo = get_object_or_404(Memo, pk=pk)

    # 소유자 확인
    if memo.user != request.user:
        raise Http404()

    if request.method == "POST":
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            memo = form.save()
            return redirect("memos:memo_detail", pk=memo.pk)
    else:
        form = MemoForm(instance=memo)

    context = {
        "form": form,
        "memo": memo,
        "page_title": u"메모 수정"
    }
    return render(request, "memos/memo_form.html", context)


@login_required(login_url="users:login")
@require_http_methods(["GET", "POST"])
def memo_delete_view(request, pk):
    """
    메모 삭제 뷰
    """
    memo = get_object_or_404(Memo, pk=pk)

    # 소유자 확인
    if memo.user != request.user:
        raise Http404()

    if request.method == "POST":
        memo.delete()
        return redirect("memos:memo_list")

    context = {
        "memo": memo,
        "page_title": u"메모 삭제"
    }
    return render(request, "memos/memo_confirm_delete.html", context)
