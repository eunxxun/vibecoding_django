# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.memo_list_view, name="memo_list"),
    url(r"^(?P<pk>\d+)/$", views.memo_detail_view, name="memo_detail"),
    url(r"^create/$", views.memo_create_view, name="memo_create"),
    url(r"^(?P<pk>\d+)/update/$", views.memo_update_view, name="memo_update"),
    url(r"^(?P<pk>\d+)/delete/$", views.memo_delete_view, name="memo_delete"),
]
