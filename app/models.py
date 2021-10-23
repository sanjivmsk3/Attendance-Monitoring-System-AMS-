from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ClockInOut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clock_in = models.DateTimeField(null=True)
    clock_out = models.DateTimeField(null=True, blank=True)
    total_hour = models.CharField(max_length=100 ,null=True, blank=True)


class BreakInOut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clock_in = models.DateTimeField(null=True)
    clock_out = models.DateTimeField(null=True, blank=True)
    total_hour = models.CharField(max_length=100 ,null=True, blank=True)


class LeaveReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)