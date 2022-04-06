from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from candidate.models import Candidate

# Create your models here.
class Recruiter(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    company_name=models.CharField(max_length=255)
    description=models.CharField(max_length=1024)
    address = models.CharField(max_length=1024)
    email=models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Make sure you enter a valid phone number")
    phonenumber=models.CharField(max_length=10,validators=[phone_regex])
    

class Jobs(models.Model):
    recruiter_id=models.ForeignKey(Recruiter,on_delete=models.CASCADE,null=True)
    jobs_id=models.AutoField(primary_key=True)
    job_title=models.CharField(max_length=155)
    min_experience=models.IntegerField(null=True,blank=True)
    max_experience=models.IntegerField(null=True,blank=True)
    min_salary=models.IntegerField(null=True,blank=True)
    max_salary=models.IntegerField(null=True,blank=True)
    location=models.CharField(max_length=255)
    qualification=models.CharField(max_length=155)
    certification=models.CharField(max_length=155)
    discription=models.CharField(max_length=255)
    vacancies_no=models.IntegerField(null=True,blank=True)
    created_datetime=models.DateTimeField(auto_now_add=True) #add joindatetime
    closing_date=models.DateField(auto_now_add=False,null=True) #add joindatetime
    status=models.CharField(max_length=50)

    def __str__(self):
        return self.job_title

class Applications(models.Model):
    candidate_id=models.ForeignKey(Candidate,on_delete=models.CASCADE,null=True)
    job_id=models.ForeignKey(Jobs,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=50,blank=True,null=True)


class Test_schedule(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    job_id=models.ForeignKey(Jobs,on_delete=models.CASCADE,null=True)
    date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    time=models.TimeField(auto_now=False, auto_now_add=False,null=True)
    description=models.CharField(max_length=1024,null=True)


class Test(models.Model):
    schedule_id=models.ForeignKey(Test_schedule,on_delete=models.CASCADE,null=True)
    candidate_id=models.ForeignKey(Candidate,on_delete=models.CASCADE,null=True)
    Applications_id=models.ForeignKey(Applications,on_delete=models.CASCADE,null=True)


class Score(models.Model):
    test_id=models.ForeignKey(Test,on_delete=models.CASCADE,null=True)
    candidate_id=models.ForeignKey(Candidate,on_delete=models.CASCADE,null=True)
    score=models.CharField(max_length=100)

class Certification_db(models.Model):
    candidate_id=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    score_id=models.ForeignKey(Score,on_delete=models.CASCADE,null=True)
    certificate_content=models.CharField(max_length=1024,null=True)