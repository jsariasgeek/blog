from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):
	user_id = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=60)
