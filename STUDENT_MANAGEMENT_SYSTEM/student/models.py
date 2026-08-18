from django.db import models


class Student(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    SEMESTER_CHOICES = [
        ('1st', '1st Semester'),
        ('2nd', '2nd Semester'),
        ('3rd', '3rd Semester'),
        ('4th', '4th Semester'),
        ('5th', '5th Semester'),
        ('6th', '6th Semester'),
        ('7th', '7th Semester'),
        ('8th', '8th Semester'),
    ]

    name = models.CharField(
        max_length=150
    )

    date_of_birth = models.DateField()

    age = models.PositiveIntegerField()

    address = models.TextField()

    roll_no = models.CharField(
        max_length=50,
        unique=True
    )

    fees_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    parents_name = models.CharField(
        max_length=150
    )

    phone_no = models.CharField(
        max_length=15
    )

    email_id = models.EmailField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    course = models.CharField(
        max_length=100
    )

    semester = models.CharField(
        max_length=10,
        choices=SEMESTER_CHOICES
    )

    image = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )

    marks = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.name} - {self.roll_no}"