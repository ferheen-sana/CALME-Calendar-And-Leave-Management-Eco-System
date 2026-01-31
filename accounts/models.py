from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('EMP', 'Employee'),
        ('MAN', 'Manager'),
    )

    EMP_ROLES = (
        ('PA', 'PA'),
        ('ENG', 'Engineer'),
        ('CON', 'Consultant'),
    )

    MAN_ROLES = (
        ('SB', 'Scientist B'),
        ('SC', 'Scientist C'),
        ('SD', 'Scientist D'),
        ('SE', 'Scientist E'),
        ('SF', 'Scientist F'),
        ('SG', 'Scientist G'),
        ('SH', 'Scientist H'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    role_type = models.CharField(
        max_length=3,
        choices=ROLE_CHOICES,
        default='EMP'
    )

    designation = models.CharField(
        max_length=50,
        choices=EMP_ROLES + MAN_ROLES
    )

    color = models.CharField(
        max_length=7,
        default="#ec4899"  # employee color (pink default)
    )

    def __str__(self):
        return f"{self.user.username} ({self.get_role_type_display()})"
