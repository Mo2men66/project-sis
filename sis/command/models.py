from django.db import models

SEMESTER_TYPE = (
        (1, 'Summer'),
        (2, 'Fall'),
        (3, 'Spring'),
)

TIMESLOTS = (
        (1, '09:00 - 10:30'),
        (2, '10:45 - 12:15'),
        (3, '12:30 - 02:00'),
        (4, '02:15 - 03:45'),
)

DAYS = (
        (1, 'Sun'),
        (2, 'Mon'),
        (3, 'Tue'),
        (4, 'Wed'),
        (5, 'Thu'),
)

class Instructor(models.Model):
    userinfo = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='instructor')

class Faculty(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Major(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    degree = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.CharField(max_length=6, unique=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    credit_hours = models.IntegerField()
    mandatory = models.BooleanField()
    faculty = models.OneToOneField(Faculty, on_delete=models.CASCADE)
    prerequisites = models.ManyToManyField('command.Course')
    minimum_level = models.PositiveSmallIntegerField(default=1)
    available = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Semester(models.Model):
    kind = models.TextField(choices=SEMESTER_TYPE)
    year = models.DateField()

class Room(models.Model):
    name = models.CharField(max_length=len('BXX-FXX-XX'))

class Timeslot(models.Model):
    day = models.TextField(choices=DAYS)
    timeslot = models.TextField(choices=TIMESLOTS)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, to_field='code')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.day} {self.timeslot}'
    
