from django.db import models

class Student(models.Model):
    userinfo = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='student')
    cgpa = models.FloatField()
    major = models.OneToOneField('command.Major', on_delete=models.SET_NULL, null=True)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey('command.Course', on_delete=models.CASCADE)
    semester = models.ForeignKey('command.Semester', on_delete=models.CASCADE)
    instructor = models.ForeignKey('command.Instructor', on_delete=models.CASCADE)
    classwork_marks = models.IntegerField()
    homework_marks = models.IntegerField()
    midterm_mark = models.IntegerField()
    final_mark = models.IntegerField()
    gpa = models.FloatField()

