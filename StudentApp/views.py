import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from StudentApp.forms import LoginForm, TeacherForm, StudentForm, TimetableForm, NotificationForm, FeedbackForm

from StudentApp.models import Teacher, Login, Student, Attendance, Timetable, Notification, Feedback


def home(request):
    return render(request, 'Admin/index.html')


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('adminview')
            elif user.is_teacher:
                return redirect('teacherhome')
            elif user.is_student:
                return redirect('studenthome')
        else:
            messages.info(request, 'invalid credentials')
    return render(request, 'Admin/login.html')


@login_required(login_url='loginview')
def adminview(request):
    return render(request, 'Admin/adminhome.html')


@login_required(login_url='loginview')
def teacher_register(request):
    login_form = LoginForm()
    teacher_form = TeacherForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        teacher_form = TeacherForm(request.POST)
        if login_form.is_valid() and teacher_form.is_valid():
            user = login_form.save(commit=False)
            user.is_teacher = True
            user.save()
            teach = teacher_form.save(commit=False)
            teach.user = user
            teach.save()
            messages.info(request, 'Teacher registration is successful')
            return redirect('teacherview')
    return render(request, 'Teacher/teacher_register.html', {'login_form': login_form, 'teacher_form': teacher_form})


@login_required(login_url='loginview')
def teacher_view(request):
    teach = Teacher.objects.all()
    return render(request, 'Teacher/teacher_view.html', {'teach': teach})


@login_required(login_url='loginview')
def teacher_update(request, id):
    teach = Teacher.objects.get(id=id)
    t = Login.objects.get(teacher=teach)
    if request.method == 'POST':
        form = TeacherForm(request.POST or None, instance=teach)
        login_form = LoginForm(request.POST or None, instance=t)
        if form.is_valid() and login_form.is_valid():
            form.save()
            login_form.save()
            messages.info(request, 'Teacher updation is successful')
            return redirect('teacherview')
    else:
        form = TeacherForm(instance=teach)
        login_form = LoginForm(instance=t)
    return render(request, 'Teacher/teacher_update.html', {'form': form, 'login_form': login_form})


def teacher_delete(request, id):
    teach = Teacher.objects.get(id=id)
    t = Login.objects.get(teacher=teach)
    if request.method == 'POST':
        t.delete()
        messages.info(request, 'Teacher deleted successfully')
        return redirect('teacherview')
    else:
        return redirect('techerview')


def logoutview(request):
    logout(request)
    return redirect('loginview')


@login_required(login_url='loginview')
def teacherhome(request):
    return render(request, 'Teacher/teacher_home.html')


@login_required(login_url='loginview')
def studentregister(request):
    login_form = LoginForm()
    student_form = StudentForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        student_form = StudentForm(request.POST)
        if login_form.is_valid() and student_form.is_valid():
            user = login_form.save(commit=False)
            user.is_student = True
            user.save()
            su = student_form.save(commit=False)
            su.user = user
            su.save()
            messages.info(request, 'student registered successfully')
            return redirect('studentview')
    return render(request, 'Student/studentregister.html', {'login_form': login_form, 'student_form': student_form})


@login_required(login_url='loginview')
def studentview(request):
    su = Student.objects.all()
    return render(request, 'Student/studentview.html', {'su': su})


@login_required(login_url='loginview')
def studentupdate(request, id):
    su = Student.objects.get(id=id)
    s = Login.objects.get(student=su)
    if request.method == 'POST':
        form = StudentForm(request.POST or None, instance=su)
        login_form = LoginForm(request.POST or None, instance=s)
        if form.is_valid() and login_form.is_valid():
            form.save()
            login_form.save()
            messages.info(request, 'Student updated successfully')
            return redirect('studentview')
    else:
        form = StudentForm(instance=su)
        login_form = LoginForm(instance=s)
    return render(request, 'Student/studentupdate.html', {'form': form, 'login_form': login_form})


def studentdelete(request, id):
    su = Student.objects.get(id=id)
    s = Login.objects.get(student=su)
    if request.method == 'POST':
        s.delete()
        messages.info(request, 'Student deleted successfully')
        return redirect('studentview')
    else:
        return redirect('studentview')


@login_required(login_url='loginview')
def studenthome(request):
    return render(request, 'Student/studenthome.html')


@login_required(login_url='loginview')
def studentprofile(request):
    u = request.user
    profile = Student.objects.filter(user_id=u)
    return render(request, 'Student/studentprofile.html', {'profile': profile})


def teacherprofile(request):
    teach = Teacher.objects.all()
    return render(request, 'Teacher/teacherprofile.html', {'teach': teach})


def add_attendance(request):
    student = Student.objects.all()
    return render(request, 'Teacher/add_attendance.html', {'student': student})


now = datetime.datetime.now()


def mark(request, id):
    user = Student.objects.get(id=id)
    att = Attendance.objects.filter(student=user, date=datetime.date.today())
    if att.exists():
        messages.info(request, "Today's attendance already marked")
        return redirect('student_attendance')
    else:
        if request.method == 'POST':
            attndc = request.POST.get('attendance')
            Attendance(student=user, date=datetime.date.today(), attendance=attndc, time=now.time()).save()
            messages.info(request, "Attendance added successfully")
            return redirect('student_attendance')
        return render(request, 'Teacher/mark_attendance.html')


def view_attendance(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    attendance = {}
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
    return render(request, 'Teacher/view_attendance.html', {'attendance': attendance})


def day_attendance(request, date):
    attendance = Attendance.objects.filter(date=date)
    context = {'attendance': attendance, 'date': date}
    return render(request, 'Teacher/day_attendance.html', context)


def add_timetable(request):
    timetable_form = TimetableForm()
    if request.method == 'POST':
        timetable_form = TimetableForm(request.POST)
        if timetable_form.is_valid():
            timetable_form.save()
            return redirect('viewtimetable')
    return render(request, 'Admin/add_timetable.html', {'timetable_form': timetable_form})


def view_timetable(request):
    tt = Timetable.objects.all()
    return render(request, 'Admin/view_timetable.html', {'tt': tt})


def timetableview_teacher(request):
    tet = Timetable.objects.all()
    return render(request, 'Teacher/view_timetable.html', {'tet': tet})


def timetableview_student(request):
    st = Timetable.objects.all()
    return render(request, 'Student/view_timetable.html', {'st': st})


def delete_timetable(request, id):
    tt = Timetable.objects.get(id=id)
    if request.method == 'POST':
        tt.delete()
        return redirect('viewtimetable')
    else:
        return redirect('viewtimetable')


def add_notification(request):
    notif_form = NotificationForm()
    if request.method == 'POST':
        notif_form = NotificationForm(request.POST)
        if notif_form.is_valid():
            notif_form.save()
            return redirect('viewnotification')
    return render(request, 'Teacher/add_notification.html', {'notif_form': notif_form})


def view_notification(request):
    n = Notification.objects.all()
    return render(request, 'Teacher/view_notification.html', {'n': n})


def delete_notification(request, id):
    no = Notification.objects.get(id=id)
    if request.method == 'POST':
        no.delete()
        return redirect('viewnotification')
    else:
        return redirect('viewnotification')


def student_notification(request):
    notif = Notification.objects.all()
    return render(request, 'Student/view_notification.html', {'notif': notif})


def add_feedback(request):
    if request.method == 'POST':
        fb_form = FeedbackForm(request.POST)
        if fb_form.is_valid():
            fb_form.save()
            return redirect('viewfeedback')
    else:
        fb_form = FeedbackForm()
    return render(request, 'Teacher/add_feedback.html', {'fb_form': fb_form})


def view_feedback(request):
    fb = Feedback.objects.all()
    return render(request, 'Teacher/view_feedback.html', {'fb': fb})


def adminview_feedback(request):
    admin_fb = Feedback.objects.all()
    return render(request, 'Admin/view_feedback.html', {'admin_fb': admin_fb})


def add_reply(request, id):
    replys = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        replys.reply = r
        replys.save()
        messages.info(request, 'Reply send for feedback')
        return redirect('adminviewfeedback')
    return render(request, 'Admin/add_reply.html', {'replys': replys})


def view_feedbackreply(request):
    fbr = Feedback.objects.all()
    return render(request, 'Teacher/view_replyfeedback.html', {'fbr': fbr})
