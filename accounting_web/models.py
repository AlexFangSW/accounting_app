from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

# Create your models here.

class Record(models.Model):
    """ 
    Record
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    discription = models.CharField(max_length=200, default='Null')
    """Discribe the cause for this record ex:Buy breakfast"""
    price = models.IntegerField(default=0)
    date = models.DateField(default=date.today())

    def __str__(self):
        return f'Accounting record : {self.discription}'
