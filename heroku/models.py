from django.db import models


class HerokuModel(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    city = models.CharField(max_length=10)
    withdrawl = models.PositiveIntegerField(default=0)
    total_money = models.PositiveIntegerField(default=0)
