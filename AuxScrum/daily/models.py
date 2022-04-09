from django.db import models
from datetime import date

class dateDaily(models.Model):
    date =  models.DateField(default=date.today, blank=True)

    def __str__(self):
        return str(self.date)

class formularioDaily(models.Model):
    date_daily = models.ForeignKey(dateDaily, on_delete=models.CASCADE)
    q1 = models.CharField(max_length=2500)
    q2 = models.CharField(max_length=2500)
    q3 = models.CharField(max_length=2500)

    def __str__(self):
        return 'Daily do dia {}'.format(str(self.date_daily))