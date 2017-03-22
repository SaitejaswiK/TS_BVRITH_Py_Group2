from django.db import models

#create your models here.
from django.db import models
from django.utils import timezone

class notifications(models.model):
 StudentId = models.ForeignKey()
 date = models.Textfield()
 notification = models.charfeild(max_length = 30)
 
 class drive(models.model):
  CompanyName = models.ForeignKey()
  title = models.charfeild(max_length = 200)
  created_date = models.DateTimeField(dafault=timezone.now)
  
