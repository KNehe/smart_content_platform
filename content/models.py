from django.db import models
from django.contrib.auth.models import User


class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    generated_text = models.TextField()
    tags = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic
