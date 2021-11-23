from django.db import models
from django.contrib.auth.models import User

class application(models.Model):

    title = models.CharField(max_length = 64)
    application_feedback = models.BooleanField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title