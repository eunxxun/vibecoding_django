# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = "memos"

urlpatterns = [
    path("", views.memo_list_view, name="memo_list"),
    path("<int:pk>/", views.memo_detail_view, name="memo_detail"),
    path("create/", views.memo_create_view, name="memo_create"),
    path("<int:pk>/update/", views.memo_update_view, name="memo_update"),
    path("<int:pk>/delete/", views.memo_delete_view, name="memo_delete"),
]
