from django.db import models
import uuid

class Essay(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField()
	key = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)