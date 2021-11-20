from django.db import models
from administrator.models import CustomUser


#from staff.models import Staffs
class SessionYearModel(models.Model):
    id=models.AutoField(primary_key=True)
    session_start_year=models.DateField()
    session_end_year=models.DateField()
    objects=models.Manager()
    
class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    staff_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255)
    course_id= models.ForeignKey(Courses, on_delete=models.DO_NOTHING,default=1)
    staff_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
 

class schoolnotice(models.Model):
    id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE,default=1)
    Notice = models.TextField()
    notice_upload=models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()