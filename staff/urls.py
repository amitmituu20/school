from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from staff import views as staffview
from school import settings

urlpatterns = [
    
    path('staff_home', staffview.staff_home, name="staff_home"),
    path('staff_take_attendance', staffview.staff_take_attendance, name="staff_take_attendance"),
    path('staff_update_attendance', staffview.staff_update_attendance, name="staff_update_attendance"),
    path('get_students', staffview.get_students, name="get_students"),
    path('get_attendance_dates', staffview.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student', staffview.get_attendance_student, name="get_attendance_student"),
    path('save_attendance_data', staffview.save_attendance_data, name="save_attendance_data"),
    path('save_updateattendance_data', staffview.save_updateattendance_data, name="save_updateattendance_data"),
    path('staff_apply_leave', staffview.staff_apply_leave, name="staff_apply_leave"),
    path('staff_apply_leave_save', staffview.staff_apply_leave_save, name="staff_apply_leave_save"),
    path('staff_profile', staffview.staff_profile, name="staff_profile"),
    path('staff_profile_save', staffview.staff_profile_save, name="staff_profile_save"),
    path('staff_fcmtoken_save', staffview.staff_fcmtoken_save, name="staff_fcmtoken_save"),
    path('staff_all_notification', staffview.staff_all_notification, name="staff_all_notification"),
    path('assignment_add', staffview.assignment_add, name="assignment_add"),
    path('add_assignment_save', staffview.add_assignment_save, name="add_assignment_save"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)