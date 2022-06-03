from django.db import models

from Subject.models import Topic

# Create your models here.
#Each quiz needs to have a pool of questions to choose from
#There needs to be 3 types of questions:
# Multiple Choice, True or False, argumentative questions 
class MultipleChoiceQuestion(models.Model):
    statement = models.CharField(max_length=250)
    opt1 = models.CharField(max_length=250, null=True)
    opt2 = models.CharField(max_length=250, null=True)
    opt3 = models.CharField(max_length=250, null=True)
    opt4 = models.CharField(max_length=250, null=True)
    ans = models.CharField(max_length=250, null=True)
    topic = models.ForeignKey(Topic)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class TrueOrFalseQuestion(models.Model):
    statement = models.CharField(max_length=250)
    opt1 = models.CharField(max_length=250, null=True)
    opt2 = models.CharField(max_length=250, null=True)
    ans = models.CharField(max_length=250, null=True)
    topic = models.ForeignKey(Topic)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)