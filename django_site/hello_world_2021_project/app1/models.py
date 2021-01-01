from django.db import models

# Create your models here.
class PersonInfo(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    roll_number = models.IntegerField()
    def __str__(self):
        return self.name
