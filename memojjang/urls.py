from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("admin/", admin.site.urls),
    path("users/", include("apps.users.urls", namespace="users")),
    path("memos/", include("apps.memos.urls", namespace="memos")),
]
