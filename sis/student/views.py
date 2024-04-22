from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, reverse

def index(req):
    return render(req, 'student/base.html', {})

def login(req):
    pass

def logout(req):
    logout(req)
    return redirect('student:index')

@login_required(login_url='student:login')
def courses(req):
    pass

@login_required(login_url='student:login')
def calender(req):
    pass

@login_required(login_url='student:login')
def gpa_calculator(req):
    pass

@login_required(login_url='student:login')
def register_course(req, course_pk):
    pass

@login_required(login_url='student:login')
def drop_course(req, course_pk):
    pass

@login_required(login_url='student:login')
def withdraw_course(req, course_pk=None):
    pass

@login_required(login_url='student:login')
def view_attendance(req):
    pass

@login_required(login_url='student:login')
def view_report(req):
    pass

@login_required(login_url='student:login')
def view_results(req):
    pass

