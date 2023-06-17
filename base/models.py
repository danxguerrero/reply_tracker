from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ticket = models.CharField(max_length=20)
    note = models.CharField(max_length=40, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ticket
    
    class Meta:
        ordering = ['created']