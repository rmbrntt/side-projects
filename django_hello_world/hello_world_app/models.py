from django.db import models

# Create your models here.
class Task(models.Model):

    name = models.CharField(max_length=100)

class UserLifts(models.Model):

    lift = models.ForeignKey('Lift')
    reps = models.IntegerField()
    sets = models.IntegerField()
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Lift(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
