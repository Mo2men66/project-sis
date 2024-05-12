from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from command.models import *
from .forms import *
from .models import *

@login_required(login_url='student:login')
def index(req):
    return render(req, 'student/home.html', {'user': req.user.student })

def logout(req):
    auth_logout(req)
    return redirect('student:index')

@login_required(login_url='student:login')
def courses(req):
    student = req.user.student
    current_semester = Semester.objects.last()

    passed_courses = student.enrollment_set.exclude(offering__semester=current_semester).filter(gpa__gte=1.7)
    passed_courses = list(map(lambda o: o.offering.course.id, passed_courses))
    registered_courses = student.enrollment_set.filter(offering__semester=current_semester)
    registered_courses = list(map(lambda o: o.offering.course.id, registered_courses))

    courses = Course.objects.exclude(Q(pk__in=passed_courses) | Q(pk__in=registered_courses)) \
            if len(passed_courses) > 0 else Course.objects.exclude(pk__in=registered_courses)

    courses = courses.exclude(pk__in=registered_courses).filter(faculty=student.major.faculty,
                                                                minimum_level__lte=student.level)

    current_enrollments = student.enrollment_set.filter(offering__semester=current_semester)

    print(f'{registered_courses=}')

    return render(req, 'student/courses.html', {'courses': courses, 'current_enrollments': current_enrollments})

@login_required(login_url='student:login')
def calender(req):
    student = req.user.student
    current_semester = Semester.objects.last()

    current_enrollments = student.enrollment_set.filter(offering__semester=current_semester)
    schedule = {f'{day[1]}': [None] * len(TIMESLOTS) for day in DAYS}

    for enrol in current_enrollments:
        timeslot = enrol.offering.timeslot_set.last()
        day = DAYS[timeslot.day - 1][1]
        if day not in schedule:
            schedule[day] = [timeslot]
            continue

        schedule[day][timeslot.timeslot - 1] = timeslot

    print(schedule)
    return render(req, 'student/calander.html', {'schedule': schedule})

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
    course = get_object_or_404(Course, pk=course_pk)
    student = req.user.student

    offering = get_object_or_404(course.offering_set, semester=Semester.objects.last())

    new_enrollment = Enrollment.objects.create(student=student, offering=offering)
    new_enrollment.save()

    return redirect('student:courses')

@login_required(login_url='student:login')
def drop_course(req, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    student = req.user.student

    enrollment = get_object_or_404(student.enrollment_set,
                                   offering__semester=Semester.objects.last(),
                                   offering__course=course)
    enrollment.delete()

    return redirect('student:courses')

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

