from django.db import models

# Create your models here.

class Technologies(models.Model):
    tech_name=models.CharField(max_length=100)
    question_mark=models.IntegerField()

class Test_questions(models.Model):
    technology_id=models.ForeignKey(Technologies,on_delete=models.CASCADE)
    question=models.CharField(max_length=1024)
    option1=models.CharField(max_length=1024)
    option2=models.CharField(max_length=1024)
    option3=models.CharField(max_length=1024)
    option4=models.CharField(max_length=1024)
    answer=models.CharField(max_length=1024)
    

    