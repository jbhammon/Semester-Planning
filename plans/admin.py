from django.contrib import admin
from plans.models import Plan, Course, AssignmentType, Assignment, Break

# Register your models here.

admin.site.register(Plan)
admin.site.register(Course)
admin.site.register(AssignmentType)
admin.site.register(Assignment)
admin.site.register(Break)
