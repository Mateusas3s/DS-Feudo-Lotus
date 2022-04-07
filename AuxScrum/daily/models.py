from django.db import models
from datetime import date

class formDaily(models.Model):
    q1 = models.CharField(max_length=2500)
    q2 = models.CharField(max_length=2500)
    q3 = models.CharField(max_length=2500)
    date =  models.DateField(default=date.today, blank=True)
    
    def __str__(self):
        return str(self.date)