from django.contrib import admin
from .models import *

admin.site.register([Semester, Room, Faculty, Course, Offering, Timeslot, Major])


