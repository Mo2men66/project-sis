from django.db import models

class Student(models.Model):
    userinfo = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='student')
    cgpa = models.FloatField()
    major = models.OneToOneField('command.Major', on_delete=models.SET_NULL, null=True)
    level = models.SmallIntegerField(default=1)
    enrolled = models.BooleanField(default=True)

    def get_academic_status(self):
        if self.cgpa > 3.7:
            return 'Excellence'
        elif self.cgpa > 3.0:
            return 'Very Good'
        elif self.cgpa > 2.3:
            return 'Good'
        elif self.cgpa > 1.7:
            return 'Pass'
        else:
            return 'Fail'

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    offering = models.ForeignKey('command.Offering', on_delete=models.DO_NOTHING)
    classwork_marks = models.IntegerField()
    homework_marks = models.IntegerField()
    midterm_mark = models.IntegerField()
    final_mark = models.IntegerField()
    gpa = models.FloatField()

