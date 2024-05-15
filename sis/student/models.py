from django.db import models

class Student(models.Model):
    userinfo = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='student')
    cgpa = models.FloatField()
    major = models.OneToOneField('command.Major', on_delete=models.SET_NULL, null=True)
    level = models.SmallIntegerField(default=1)
    enrolled = models.BooleanField(default=True)

    def __str__(self):
        return f'Student: {self.userinfo.first_name} {self.userinfo.last_name} - {self.major}'

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
    classwork_marks = models.IntegerField(default=0)
    homework_marks = models.IntegerField(default=0)
    midterm_mark = models.IntegerField(default=0)
    final_mark = models.IntegerField(default=0)
    gpa = models.FloatField(default=0)

    def __str__(self):
        return f'{self.student} | {self.offering}'

class Absense(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

class WithdrawRequest(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)


