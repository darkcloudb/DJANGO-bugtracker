from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

ticket_status_choices = (
    ('New', 'New'),
    ('Progress', 'In Progress'),
    ('Done', 'Done'),
    ('Invalid', 'Invalid')
)


class Author(AbstractUser):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Ticket(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    create_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author', null=True, default=None)
    ticket_status = models.CharField(max_length=15, choices=ticket_status_choices, default='New')
    assigned_to = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='assigned_to', null=True, blank=True)
    closed_by = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='closed_by', null=True, blank=True)

    def __str__(self):
        return self.title
