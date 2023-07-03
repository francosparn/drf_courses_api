from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    # Fields displayed in the Django admin table
    list_display = (
        'id',
        'name',
        'lastname',
        'email',
        'gender'
    )
    
    # Filter students by gender
    list_filter = ['gender']
    
    # Search students by last name
    search_fields = ['lastname']
    
    # Will display 10 students per page
    list_per_page = 10
    
admin.site.register(Student, StudentAdmin)