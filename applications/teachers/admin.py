from django.contrib import admin

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    # Fields displayed in the Django admin table
    list_display = (
        'id',
        'name',
        'lastname',
        'email',
        'gender'
    )
    
    # Filter teachers by gender
    list_filter = ['gender']
    
    # Search teachers by last name
    search_fields = ['lastname']
    
    # Will display 10 teachers per page
    list_per_page = 10
    
admin.site.register(Teacher, TeacherAdmin)
