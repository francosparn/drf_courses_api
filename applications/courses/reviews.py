from django.db import models
from django.db.models import Avg


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = models.IntegerField(
        'Rating',
        choices=RATING_CHOICES,
        blank=True
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    comment = models.TextField(
        'Comment',
        blank=True,
        null=True
    )
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    
    class Meta:
        verbose_name_plural = 'Reviews'
        unique_together = ('course', 'student')
        
    
    # Save reviews and calculate and update course rating
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.course.average_rating = self.course.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
        self.course.save()