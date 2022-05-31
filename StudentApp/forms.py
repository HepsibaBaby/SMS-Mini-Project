import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from StudentApp.models import Login, Teacher, Student, Timetable, Notification, Feedback, Attendance


class DateInput(forms.DateInput):
    input_type = 'date'

def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is not a valid Phone number')

class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')

class TeacherForm(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])


    class Meta:
        model = Teacher
        fields = ('name','email','contact_no','subject')

class StudentForm(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Student
        fields = ('name','standard','email','contact_no')

class TimetableForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Timetable
        fields = '__all__'

class NotificationForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Notification
        fields = '__all__'

class FeedbackForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Feedback
        fields = ('name','subject','description','date')

class AddAttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = '__all__'






