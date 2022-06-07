from django.db import models

from Subject.models import Topic

# Create your models here.
#Each quiz needs to have a pool of questions to choose from
#There needs to be 3 types of questions:
# Multiple Choice, True or False, argumentative questions 
class Question(models.Model):
    MULTIPLE = 'MU'
    TRUEFALSE = 'TF'
   
    QUESTION_TYPE_CHOICES = [
        (MULTIPLE, 'Multiple Choice'),
        (TRUEFALSE, 'True or False')   
    ]
    statement = models.CharField(max_length=250)
    opt1 = models.CharField(max_length=250, null=True)
    opt2 = models.CharField(max_length=250, null=True)
    opt3 = models.CharField(max_length=250, null=True)
    opt4 = models.CharField(max_length=250, null=True)
    ans = models.CharField(max_length=250, null=True)
    topic = models.ForeignKey(Topic)
    qtype = models.CharField(choices=QUESTION_TYPE_CHOICES, max_length=2, default=MULTIPLE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
