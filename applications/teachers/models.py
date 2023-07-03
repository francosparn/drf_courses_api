from django.db import models


class Teacher(models.Model):
    GENDER_CHOICES = [
        ("Female", "Female"),
        ("Male", "Male"),
        ("Other", "Other")
    ]
    name = models.CharField(
        'First name',
        max_length=50
    )
    lastname = models.CharField(
        'Last name',
        max_length=50
    )
    email = models.EmailField(
        'Email Address',
        unique=True,
        max_length=80
    )
    gender = models.CharField(
        'Gender',
        choices=GENDER_CHOICES,
        max_length=6
    )
    
    class Meta:
        verbose_name_plural = 'Teachers'
    
    def __str__(self):
        return self.name + ' ' + self.lastname