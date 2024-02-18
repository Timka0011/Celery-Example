from django.db import models

# Create your models here.


class Sender(models.Model):
    subject = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.email
