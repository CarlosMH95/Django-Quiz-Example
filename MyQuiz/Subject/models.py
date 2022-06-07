from django.db import models

from Subject.custom_validators import validate_min_max

# Create your models here.
#Each test should be about only 1 topic, unless its an special exam
class Subject(models.Model):
    subject_name = models.CharField(max_length=150)
    passing_percentage = models.FloatField(validators=[validate_min_max])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#Each subject has a list of topics
class Topic(models.Model):
    topic_name = models.CharField(max_length = 150)
    subject = models.ForeignKey(Subject)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)