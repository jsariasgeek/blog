from django.db import models
from tinymce.models import HTMLField
from django.conf import settings


User = settings.AUTH_USER_MODEL


# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length=30)
	abstract = models.CharField(max_length=60)
	content = HTMLField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	creation_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title