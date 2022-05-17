from django.db import models
from django.utils import timezone



class Todo(models.Model):
        content = models.TextField(
        blank=False,
        null=False,)

        created_at = models.DateTimeField(
                "作成日", default=timezone.now)

