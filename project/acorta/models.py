from django.db import models

# Create your models here.

class urls(models.Model):
	url_real = models.CharField(max_length=200)
	url_short = models.IntegerField()
