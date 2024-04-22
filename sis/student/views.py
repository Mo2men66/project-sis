from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout as auth_logout
from django.shortcuts import render, redirect, reverse

@login_required(login_url='student:login')
def index(req):
    return render(req, 'student/home.html', {})

def login(req):
    if req.method == 'GET':
        return render(req, 'student/login.html', {})


def logout(req):
    auth_logout(req)
    return redirect('student:index')

@login_required(login_url='student:login')
def courses(req):
    return render(req, 'student/courses.html', {})

@login_required(login_url='student:login')
def calender(req):
    return render(req, 'student/calander.html', {})

@login_required(login_url='student:login')
def gpa_calculator(req):
    return render(req, 'student/gpa_calculator.html', {})

@login_required(login_url='student:login')
def payment(req):
    return render(req, 'student/payment.html', {})

@login_required(login_url='student:login')
def profile(req):
    return render(req, 'student/profile.html', {})

@login_required(login_url='student:login')
def update_profile(req):
    return render(req, 'student/update.html', {})

@login_required(login_url='student:login')
def register_course(req, course_pk):
    return render(req, 'student/register.html', {})

@login_required(login_url='student:login')
def drop_course(req, course_pk):
    pass

@login_required(login_url='student:login')
def withdraw_course(req, course_pk=None):
    return render(req, 'student/withdraw.html', {})

@login_required(login_url='student:login')
def view_attendance(req):
    return render(req, 'student/attendance.html', {})

@login_required(login_url='student:login')
def view_report(req):
    return render(req, 'student/report.html', {})

@login_required(login_url='student:login')
def view_results(req):
    return render(req, 'student/result.html', {})

