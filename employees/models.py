from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    department = models.CharField(max_length=120)
    email = models.EmailField(unique=True)  # unique at DB level, too

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Custom method: Return full name in uppercase
    def full_name_upper(self):
        return (self.name or "").upper()

    def __str__(self):
        return f"{self.name} ({self.role})"
