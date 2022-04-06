from django.db import models

# for importing auth_user table
from django.contrib.auth.models import User

# Create your models here.

class Extend_usermodel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=50)

    def __str__(self):
        return self.role




