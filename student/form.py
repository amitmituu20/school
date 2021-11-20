
from django import forms

from classes.models import Courses

class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    first_name=forms.CharField(label="Full Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    dob=forms.DateField(label="date of birth",widget=DateInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Admission number",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    courses=Courses.objects.all()
    course_list=[]
    for course in courses:
        small_course=(course.id,course.course_name)
        course_list.append(small_course)

    # classes=Class.object.all()
    # classlist=[]
    # for course in courses:
    #     small_class=(Class.id,Class.class_name,Class.div)
    #     Class_list.append(small_class)

    gender_choice=(
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others")
    )

    course=forms.ChoiceField(label="Class",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
    # classes=forms.ChoiceField(label="Class",choices=Class_list,widget=forms.Select(attrs={"class":"form-control"}))
    sex=forms.ChoiceField(label="gender",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    
class EditStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,required=False,widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="Full Name",max_length=50,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Admission number",max_length=50,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address",max_length=50,required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    relegion=forms.CharField(label="relegion",max_length=50,required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    caste=forms.CharField(label="caste",max_length=50,required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    courses=Courses.objects.all()
    course_list=[]
    for course in courses:
        small_course=(course.id,course.course_name)
        course_list.append(small_course)

    gender_choice=(
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others")
    )

    course=forms.ChoiceField(label="Class",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
    sex=forms.ChoiceField(label="Gender",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)