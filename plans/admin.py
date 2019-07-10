from django.contrib import admin
from plans.models import User, Plan, Course, AssignmentType, Assignment, DaysOff

# Register your models here.

admin.site.register(User)
admin.site.register(Plan)
admin.site.register(Course)
admin.site.register(AssignmentType)
admin.site.register(Assignment)
admin.site.register(DaysOff)
