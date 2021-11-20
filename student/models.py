from django.db import models
from administrator.models import CustomUser
from classes.models import Courses,Subjects,SessionYearModel
class Students(models.Model):
    studentname=models.CharField(max_length=255) 
    status=models.BooleanField(default=False)   
    admissionno=models.CharField(max_length=255)
    bdate=models.DateField(max_length=8)
    gender=models.CharField(max_length=255)
    address=models.TextField()
    adhar_no=models.CharField(max_length=26)
    mobileno=models.CharField(max_length=10)
    parents_mobileno1=models.CharField(max_length=10)
    parents_mobileno2=models.CharField(max_length=10)
    parents_email=models.CharField(max_length=255)
    mothername=models.CharField(max_length=100)
    motheroccupation=models.CharField(max_length=100)
    motherincome=models.CharField(max_length=100)
    fathername=models.CharField(max_length=255)
    fatheroccupation=models.CharField(max_length=255)
    fatherincome=models.CharField(max_length=255)
    relegion=models.CharField(max_length=26)
    caste=models.CharField(max_length=26)
    staffchild_status=models.BooleanField(default=False)
    country=models.CharField(max_length=26)
    state=models.CharField(max_length=26)
    district=models.CharField(max_length=26)
    blood_group=models.CharField(max_length=26)
    language_group=models.CharField(max_length=26)
    mother_tounge=models.CharField(max_length=26)
    email=models.CharField(max_length=255)
    profile_pic=models.FileField()
    id=models.AutoField(primary_key=True)
    course_id= models.ForeignKey(Courses, on_delete=models.CASCADE)
    session_id= models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Students_bulk(models.Model):
    id=models.AutoField(primary_key=True)
    csv_file=models.FileField()    
    objects = models.Manager()

class  LeaveReportStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE) 
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()    

class result(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.DO_NOTHING,default=1)
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    mark=models.CharField(max_length=255)
    total_mark=models.CharField(max_length=255)
    mark_percentage=models.CharField(max_length=255)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)    



class studentnotice(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE,default=1)
    Notice = models.TextField()
    notice_upload=models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.DO_NOTHING,default=1)
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING,default=1)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    attendance_date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()    

class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.DO_NOTHING,default=1)
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING,default=1)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING,default=1)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

