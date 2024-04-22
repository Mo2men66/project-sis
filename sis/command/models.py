from django.db import models

SEMESTER_TYPE = (
        (1, 'Summer'),
        (2, 'Fall'),
        (3, 'Spring'),
)

class Instructor(models.Model):
    userinfo = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='instructor')

class Faculty(models.Model):
    name = models.CharField(max_length=250)

class Major(models.Model):
    faculty = models.OneToOneField(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    degree = models.CharField(max_length=250)

class Course(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    credit_hours = models.IntegerField()
    mandatory = models.BooleanField()
    faculty = models.OneToOneField(Faculty, on_delete=models.CASCADE)

class Semester(models.Model):
    kind = models.TextField(choices=SEMESTER_TYPE)
    year = models.DateField()


