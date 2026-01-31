from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
import random

SAFE_COLORS = [
    "#ec4899",  # pink
    "#3b82f6",  # blue
    "#8b5cf6",  # violet
    "#14b8a6",  # teal
    "#f97316",  # orange
    "#6366f1",  # indigo
]

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            role_type='EMP',
            designation='PA',
            color=random.choice(SAFE_COLORS)
        )


        
