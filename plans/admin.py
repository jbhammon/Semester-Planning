from django.contrib import admin
from plans.models import Plan, Course, AssignmentType, Assignment, Break

# Register your models here.

admin.site.register(Plan)
admin.site.register(Course)
admin.site.register(AssignmentType)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'due_date')

@admin.register(Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date')
