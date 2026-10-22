from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 5. complaint_type choices:
#    - Cleanliness
#    - Staff Behavior
#    - Waiting Time
#    - Billing
#    - Equipment

# 6. priority choices:
#    - Low
#    - Medium
#    - High
#    - Critical

# 7. status choices:
#    - Submitted
#    - Under Review
#    - In Progress
#    - Resolved

class Complaints(models.Model):
    COMPLAINT_TYPES=[
        ('CLEANLINESS','cleanliness'),
        ('STAFF BEHAVIOUR','staff behaviour'),
        ('WAITING TIME','waiting time'),
        ('BILLING','billing'),
        ('EQUIPMENT','equipment')
        
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('SUBMITTED', 'Submitted'),
        ('UNDER REVIEW', 'Under Review'),
        ('IN PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    complaint_type = models.CharField(
        max_length=30,
        choices=COMPLAINT_TYPES
    )

    department = models.CharField(max_length=100)

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Submitted'
    )

    reported_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,null=True,blank=True
    )

    def __str__(self):
        return self.title
   

