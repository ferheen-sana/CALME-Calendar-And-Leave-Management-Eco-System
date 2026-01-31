from django.contrib import admin
from .models import Leave, Notification

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = (
    'user',
    'leave_type',
    'start_date',
    'end_date',
    'status',
)
    list_filter = ("status", "leave_type", "applied_on")
    search_fields = ("user__username",)
    ordering = ("-applied_on",)

    actions = ["mark_notified_false"]

    def mark_notified_false(self, request, queryset):
        queryset.update(notified=False)

    mark_notified_false.short_description = "Reset notification (send again)"


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "is_read", "created_at")
    list_filter = ("is_read",)
    search_fields = ("user__username", "title")
