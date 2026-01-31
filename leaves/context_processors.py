from .models import Leave

def manager_notification_count(request):
    if request.user.is_authenticated:
        return {
            "manager_pending_count": Leave.objects.filter(status="Pending").count()
        }
    return {}
