# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Memo


class MemoAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "created_at", "updated_at"]
    search_fields = ["title", "content", "user__username"]
    list_filter = ["created_at", "updated_at", "user"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = (
        (None, {
            "fields": ("user", "title", "content")
        }),
        ("타임스탬프", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )


admin.site.register(Memo, MemoAdmin)
