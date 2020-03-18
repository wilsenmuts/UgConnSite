from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class litoangel(models.Model):
    lito_title = models.CharField(max_length=100)
    lito_text = models.TextField()
    lito_date = models.DateTimeField(auto_now_add=True)
    lito_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural ='litoangels'

    def __str__(self):
        return f'{self.lito_title}'