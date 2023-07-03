from django.db import models

from applications.teachers.models import Teacher

from .categories import Category
from .reviews import Review


class Course(models.Model):
    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Spanish', 'Spanish')
    ]
    name = models.CharField(
        'Name', 
        max_length=100,
        unique=True
    )
    image = models.ImageField(
        upload_to='courses',
        max_length=100,
        null=True,
        blank=True
    )
    description = models.TextField(
        'Description',
        null=True,
        blank=True
    )
    duration = models.DurationField(
        'Duration'
    )
    price = models.DecimalField(
        'Price',
        max_digits=6,
        decimal_places=2
    )
    language = models.CharField(
        'Language',
        choices=LANGUAGE_CHOICES,
        max_length=7
    )
    update_at = models.DateField(
        'Update at',
        auto_now=True
    )
    teacher = models.ForeignKey(
        Teacher, 
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'courses.Category', 
        on_delete=models.CASCADE
    )
    average_rating = models.DecimalField(
        'Average Rating',
        max_digits=3,
        decimal_places=2,
        default=0
    )

    class Meta:
        verbose_name_plural = 'Courses'
        
    def __str__(self):
        return self.name
    
