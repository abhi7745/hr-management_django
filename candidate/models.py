from django.db import models

# for importing auth_user table
from django.contrib.auth.models import User

# Create your models here.

class Candidate(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    experience_level=models.CharField(max_length=150) # experienced/fresher
    companies_experience=models.CharField(max_length=255)
    year_of_exp=models.IntegerField(null=True) # number of years
    current_ctc=models.CharField(max_length=255)
    expected_ctc=models.CharField(max_length=255)
    # serving_notice_period=models.IntegerField(null=True) # number of years
    notice_period_from=models.DateField(auto_now=False, auto_now_add=False, null=True)
    notice_period_to=models.DateField(auto_now=False, auto_now_add=False, null=True)
    willingtowork_shifts=models.CharField(max_length=50) # yes/no
    willingtowork_contract=models.CharField(max_length=50) # yes/no
    qualification=models.CharField(max_length=255)
    address=models.CharField(max_length=1024)
    primary_skill=models.CharField(max_length=150)
    secondary_skill=models.CharField(max_length=150)
    other_skill=models.CharField(max_length=150)
    primary_skill_rating=models.IntegerField(null=True) # rating out of 5
    secondary_skill_rating=models.IntegerField(null=True) # rating out of 5
    other_skill_rating=models.IntegerField(null=True) # rating out of 5
    certification=models.CharField(max_length=255)
    agreement=models.CharField(max_length=30) # agree/reject

    def __str__(self):
        return self.email