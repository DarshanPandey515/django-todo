from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class todo(models.Model):
    WORK_STATUS = [
        ('Completed','Completed'),
        ('Pending','Pending'),
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date = models.DateTimeField(auto_now_add=True,null=True)
    Work_Status = models.CharField(choices=WORK_STATUS,max_length=50,default='Pending')
