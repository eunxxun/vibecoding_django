from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.home_view, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^users/", include("apps.users.urls", namespace="users")),
    url(r"^memos/", include("apps.memos.urls", namespace="memos")),
]
