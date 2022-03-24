from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

class Record(models.Model):
    """ 
    Record
    """
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    CHOICES = [
        ('支出', '支出'),
        ('收入', '收入')
    ]
    income_or_expense = models.CharField(
        max_length=2,
        choices=CHOICES,
        default='支出'
    )

    tag_name = models.ForeignKey('Tag', on_delete=models.CASCADE)
    """Classification of records ex:food...etc"""

    discription = models.CharField(max_length=200, default='Null')
    """Further discribe the cause for this record ex:sandwich and milk"""

    price = models.IntegerField(default=0)

    date = models.DateField(default=date.today())

    def __str__(self):
        return f'Accounting record : {self.discription}'

class Tag(models.Model):
    """
    Tag for easy classification of records.
    """
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default='')

    CHOICES = [
        ('支出', '支出'),
        ('收入', '收入')
    ]
    income_or_expense = models.CharField(
        max_length=2,
        choices=CHOICES,
        default='支出'
    )

    tag_name = models.CharField(max_length=200, default='早餐', unique=True)

    def __str__(self):
        return f'{self.tag_name}'