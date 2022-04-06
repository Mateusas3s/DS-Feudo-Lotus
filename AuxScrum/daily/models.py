from django.db import models

class formDaily(models.Model):
    q1 = models.CharField(max_length=2500)
    q2 = models.CharField(max_length=2500)
    q3 = models.CharField(max_length=2500)
    
    def __str__(self):
        return('O que eu fiz hoje?\n{}\nQuais foram os impedimentos?\n{}\nO que pretendo fazer?\n{}'.format(self.q1, self.q2, self.q3))