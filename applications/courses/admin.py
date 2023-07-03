from django.contrib import admin

from .models import Course, Review
from .categories import Category


class CourseAdmin(admin.ModelAdmin):
    # Fields displayed in the Django admin table
    list_display = (
        'id',
        'name',
        'duration',
        'price',
        'language',
        'update_at',
        'teacher',
        'category',
        'average_rating'
    )
    
    # Filter courses by language or teacher
    list_filter = ['language', 'teacher', 'category']
    
    # Will display 10 courses per page
    list_per_page = 10
    
admin.site.register(Course, CourseAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'created_at',
        'update_at'
    )

admin.site.register(Category, CategoryAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'rating',
        'course',
        'student'
    )

admin.site.register(Review, ReviewAdmin)
