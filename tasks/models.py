from django.db import models
from django.contrib.auth.models import User





class TaskGroup(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'user'],
                name='unique_group_per_user'
            )
        ]


class Tasks(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=False
    )
    group = models.ForeignKey(
        TaskGroup,
        on_delete=models.CASCADE,
        null=True,
        related_name='tasks'
    )
    description = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )
    due_date = models.DateField(null=True)
    
    
    def save(self, *args, **kwargs):
        # If no group is specified, assign to "General" group
        if not self.group:
            general_group, _ = TaskGroup.objects.get_or_create(
                name="General",
                user=self.user,
                defaults={'description': 'Default group for ungrouped tasks'}
            )
            self.group = general_group
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


