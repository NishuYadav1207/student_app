from django.contrib import admin

from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'roll_no',
        'course',
        'semester',
        'gender',
        'marks',
        'fees_amount',
    )

    search_fields = (
        'name',
        'roll_no',
        'email_id',
        'course',
    )

    list_filter = (
        'gender',
        'course',
        'semester',
    )