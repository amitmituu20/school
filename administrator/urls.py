from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from administrator import adminview,views
from school import settings
urlpatterns = [
    
    path('demo',views.demo),
    path('admin/', admin.site.urls),
    path('',views.showlogin,name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.dologin,name="do_login"),
    path('admin_home',adminview.admin_home,name="admin_home"),    
    #path('admin_home',views.admin_home,name="admin_home"),
    path('add_student_save',adminview.add_student_save,name="add_student_save"),
    path('add_bulk_student',adminview.add_bulk_student,name="add_bulk_student"),
    path('add_bulk_student_save',adminview.add_bulk_student_save,name="add_bulk_student_save"),
    path('add_staff_save',adminview.add_staff_save,name="add_staff_save"),
    path('add_course_save', adminview.add_course_save,name="add_course_save"),
    path('add_subject_save', adminview.add_subject_save,name="add_subject_save"),
    path('manage_class_subject_staff', adminview.manage_class_subject_staff, name="manage_class_subject_staff"),
    path('manage_staff', adminview.manage_staff, name="manage_staff"),
    path('manage_student', adminview.manage_student, name="manage_student"),
    path('manage_student', adminview.manage_student,name="manage_student"),
    path('manage_course', adminview.manage_course, name="manage_course"),
    path('manage_subject', adminview.manage_subject, name="manage_subject"),
    path('manage_session', adminview.manage_session, name="manage_session"),
    path('manage_student_filter', adminview.manage_student_filter,name="manage_student_filter"),
    path('edit_student/<str:student_id>', adminview.edit_student,name="edit_student"),
    path('edit_staff/<str:staff_id>', adminview.edit_staff, name="edit_staff"),
    path('delete_student/<str:student_id>', adminview.delete_student,name="delete_student"),
    path('delete_class/<str:class_id>', adminview.delete_class, name="delete_class"),
    path('delete_sub/<str:sub_id>', adminview.delete_subject, name="delete_sub"),
    path('delete_staff/<str:staff_id>', adminview.delete_staff, name="delete_staff"),
    path('edit_student_save', adminview.edit_student_save,name="edit_student_save"),
    path('edit_staff_save', adminview.edit_staff_save, name="edit_staff_save"),
    path('student_leave_view', adminview.student_leave_view,name="student_leave_view"),
    path('staff_leave_view', adminview.staff_leave_view,name="staff_leave_view"),
    path('admin_view_attendance', adminview.admin_view_attendance,name="admin_view_attendance"),
    path('admin_send_notification_staff', adminview.admin_send_notification_staff,name="admin_send_notification_staff"),
    path('admin_send_notification_student', adminview.admin_send_notification_student,name="admin_send_notification_student"),
    

     
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)