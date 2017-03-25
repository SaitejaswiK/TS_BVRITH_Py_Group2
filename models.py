from django.db import models

# Create your models here.

class TPO(models.Model):
    drive_name = models.CharField(max_length = 20)
    TPO_notification = models.CharField(max_length = 200)
