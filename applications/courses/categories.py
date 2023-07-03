from django.db import models


class Category(models.Model):
    name = models.CharField(
        'Category',
        max_length=80
    )
    created_at = models.DateTimeField(
        'Created at',
        auto_now_add=True
    )
    update_at = models.DateTimeField(
        'Update at',
        auto_now=True
    )
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name