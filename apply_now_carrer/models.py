from django.db import models

class JobApplication(models.Model):
    resume = models.FileField(upload_to='resumes/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_phone = models.CharField(max_length=15)
    experience_years = models.PositiveIntegerField()
    experience_months = models.PositiveIntegerField()
    current_salary = models.PositiveIntegerField()
    expected_salary = models.PositiveIntegerField()
    available_to_join = models.PositiveIntegerField()
    privacy_policy = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
