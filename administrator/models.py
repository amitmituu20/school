from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class CustomUser(AbstractUser):
    user_type_data=((1,"admin"),(2,"Staff"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

