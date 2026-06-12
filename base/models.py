from django.db import models
from django.contrib.auth.models import User
import uuid

class Essay(models.Model):
	title = models.CharField(max_length=250)
	paragraphs = models.IntegerField(default=3)
	grade_level = models.CharField(max_length=250)
	content = models.TextField()
	key = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)