from django.db import models



class Todo(models.Model):
        content = models.TextField(
        blank=False,
        null=False,)
