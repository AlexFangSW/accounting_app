from django.db import models
from django.contrib.auth import get_user_model
from django.forms import CharField
from django.utils import timezone

# Create your models here.

class Record(models.Model):

    user_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    activaty = CharField(max_length=200)
    price = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'Accounting record : {self.activaty}'
