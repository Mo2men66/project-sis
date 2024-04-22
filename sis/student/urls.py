from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
        path('', views.index, name='index'),
        path('login', views.login, name='login'),
        path('logout', views.logout, name='logout'),
        path('calender', views.calender, name='calender'),
        path('attendence/view', views.view_attendance, name='view_attendence'),
        path('courses', views.courses, name='courses'),
        path('courses/register', views.register_course, name='register_course'),
        path('courses/withdraw', views.withdraw_course, name='withdraw_course'),
        path('courses/withdraw/<int:course_pk>', views.withdraw_course, name='withdraw_course'),
        path('report', views.view_report, name='report'),
        path('gpa', views.gpa_calculator, name='gpa'),
        path('results', views.view_results, name='results'),
        path('payment', views.payment, name='payment'),
        path('profile', views.profile, name='profile'),
        path('profile/update', views.update_profile, name='update_profile'),
]

