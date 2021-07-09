from django.db import models

class partner(models.Model):
    name = models.CharField(max_length=50, default="")
    logo = models.ImageField(upload_to="partners")
    notes = models.TextField(blank=True)
    timer = models.DateTimeField(auto_now_add=False)