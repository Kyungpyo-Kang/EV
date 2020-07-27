from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=50)
    member_email = models.CharField(max_length=50)
