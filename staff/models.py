from django.db import models
from administrator.models import CustomUser
from classes.models import Courses,Subjects
# Create your models here.
class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    adhar_no=models.CharField(max_length=26)
    mother_tounge=models.CharField(max_length=26)
    email=models.CharField(max_length=255)
    mobileno=models.CharField(max_length=10)
    relegion=models.CharField(max_length=26)
    caste=models.CharField(max_length=26)
    status=models.BooleanField(default=False)
    marital_status=models.CharField(max_length=26)
    qualification=models.CharField(max_length=26)
    profile_pic=models.FileField(default=False)
    country=models.CharField(max_length=26)
    state=models.CharField(max_length=26)
    district=models.CharField(max_length=26)
    blood_group=models.CharField(max_length=26)
    address=models.TextField()
    gender=models.CharField(max_length=255)
    sbdate=models.DateField(max_length=8)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    sub_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    objects=models.Manager()
   
class LeaveReportStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()   

class NotificationStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()    


class assignment(models.Model):
    id=models.AutoField(primary_key=True)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE,default=1)
    subject_id=models.ForeignKey(Subjects,on_delete=models.CASCADE,default=1)
    staff_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=1)
    assign_name=models.CharField(max_length=25)
    assign_text=models.CharField(max_length=255)
    assign_upload=models.FileField()
    dates=models.DateTimeField(auto_now_add=True)
    times=models.TimeField(auto_now_add=True)
    State=models.BooleanField(default=False)

class Subjectstaff(models.Model):
    id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    objects = models.Manager()