from django.db import models
from django.contrib.auth.models import User

# ================== CONSTANTS ==================
LEAVE_TYPES = (
    ("CL", "Casual Leave"),
    ("RH", "Restricted Holiday"),
)

LEAVE_STATUS = (
    ("PENDING", "Pending"),
    ("APPROVED", "Approved"),
    ("REJECTED", "Rejected"),
)

class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=5, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=LEAVE_STATUS,
        default="PENDING"
    )

    applied_on = models.DateTimeField(auto_now_add=True)
    decision_on = models.DateTimeField(null=True, blank=True)
    notified = models.BooleanField(default=False)
    leave_type = models.CharField(max_length=2)  # CL / RH
    reason = models.TextField()

    @property
    def total_days(self):
        return (self.end_date - self.start_date).days + 1

    def __str__(self):
        return f"{self.user.username} - {self.leave_type}"


# ================== LEAVE BALANCE MODEL ==================
class LeaveBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cl_balance = models.FloatField(default=8)
    rh_balance = models.FloatField(default=2)

    def __str__(self):
        return self.user.username


# ================== NOTIFICATION MODEL ==================
class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"


# ================== MEETING MODEL ==================
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # <-- add this
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    repeat = models.CharField(
        max_length=20,
        choices=[
            ("none", "None"),
            ("daily", "Daily"),
            ("weekly", "Weekly"),
        ],
        default="none"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def status(self):
        from django.utils.timezone import now
        if self.end and self.end < now():
            return "completed"
        if self.start.date() == now().date():
            return "today"
        return "upcoming"
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    repeat = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=[('approved','Approved'),('pending','Pending')],
        default='approved'
    )

class LeaveFileCounter(models.Model):
    year = models.IntegerField(unique=True)
    last_number = models.IntegerField(default=0)

    @classmethod
    def next_file_number(cls):
        from datetime import datetime
        year = datetime.now().year

        obj, created = cls.objects.get_or_create(year=year)
        obj.last_number += 1
        obj.save()

        return f"{year}/HR/{obj.last_number:05d}"

