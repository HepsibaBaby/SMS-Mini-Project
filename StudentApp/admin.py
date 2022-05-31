from django.contrib import admin

# Register your models here.
from StudentApp import models

admin.site.register(models.Login)
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.Attendance)
admin.site.register(models.Timetable)
admin.site.register(models.Notification)
admin.site.register(models.Feedback)


