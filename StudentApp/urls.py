from django.urls import path

from StudentApp import views


urlpatterns = [
    path('',views.home,name='home'),
    path('loginview',views.loginview,name='loginview'),
    path('adminview',views.adminview,name='adminview'),
    path('teacherregister',views.teacher_register,name='teacherregister'),
    path('teacherview',views.teacher_view,name='teacherview'),
    path('teacherupdate/<int:id>',views.teacher_update,name='teacherupdate'),
    path('teacherdelete/<int:id>',views.teacher_delete,name='teacherdelete'),
    path('logoutview',views.logoutview,name='logoutview'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('studentregister',views.studentregister,name='studentregister'),
    path('studentview',views.studentview,name='studentview'),
    path('studentupdate/<int:id>',views.studentupdate,name='studentupdate'),
    path('studentdelete/<int:id>',views.studentdelete,name='studentdelete'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('studentprofile',views.studentprofile,name='studentprofile'),
    path('teacherprofile',views.teacherprofile,name='teacherprofile'),
    path('student_attendance',views.add_attendance,name='student_attendance'),
    path('marks/<int:id>',views.mark,name='marks'),
    path('view_attendance',views.view_attendance,name='view_attendance'),
    path('day_attendance/<date>',views.day_attendance,name='day_attendance'),
    path('addtimetable',views.add_timetable,name='addtimetable'),
    path('viewtimetable',views.view_timetable,name='viewtimetable'),
    path('teacherviewtimetable',views.timetableview_teacher,name='teacherviewtimetable'),
    path('studentviewtimetable', views.timetableview_student, name='studentviewtimetable'),
    path('timetable_delete/<int:id>',views.delete_timetable,name='timetable_delete'),
    path('addnotification',views.add_notification,name='addnotification'),
    path('viewnotification',views.view_notification,name='viewnotification'),
    path('delete_notification/<int:id>',views.delete_notification,name='delete_notification'),
    path('studentnotification',views.student_notification,name='studentnotification'),
    path('addfeedback',views.add_feedback,name='addfeedback'),
    path('viewfeedback',views.view_feedback,name='viewfeedback'),
    path('adminviewfeedback',views.adminview_feedback, name='adminviewfeedback'),
    path('addreply/<int:id>',views.add_reply,name='addreply'),
    path('replyfeedback',views.view_feedbackreply,name='replyfeedback')



]