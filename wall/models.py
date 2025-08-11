from django.db import models

class Note(models.Model):
    COLOR_CHOICES = [
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('pink', 'Pink'),
        ('orange', 'Orange'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='yellow')
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
