from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Plan(models.Model):
    name         = models.CharField(max_length=200, help_text='Plan Name')
    user         = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    current_plan = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Course(models.Model):
    title   = models.CharField(max_length=200, help_text='Title or Number of the course')
    plan_id = models.ForeignKey('Plan', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class AssignmentType(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the type of assignment')
    course_id = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    name = models.CharField(max_length=200, help_text='Assignment Name')
    type_id = models.ForeignKey('AssignmentType', on_delete=models.SET_NULL, null=True)
    course_id = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    due_date = models.DateField()
    hours_expected = models.DecimalField(max_digits=5, decimal_places=2)
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.name

class Break(models.Model):
    plan_id    = models.ForeignKey('Plan', on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date   = models.DateField()

    def __str__(self):
        return str(self.id)
