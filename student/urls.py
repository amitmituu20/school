from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from student import views as studentsview
from school import settings

urlpatterns = [
    
    path('student_home', studentsview.student_home, name="student_home"),
    path('student_view_attendance', studentsview.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post', studentsview.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_apply_leave', studentsview.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save', studentsview.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_profile', studentsview.student_profile, name="student_profile"),
    path('student_profile_save', studentsview.student_profile_save, name="student_profile_save"),
    path('student_fcmtoken_save', studentsview.student_fcmtoken_save, name="student_fcmtoken_save"),
    path('student_all_notification',studentsview.student_all_notification,name="student_all_notification"),
    path('student_view_result',studentsview.student_view_result,name="student_view_result"),

 ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)