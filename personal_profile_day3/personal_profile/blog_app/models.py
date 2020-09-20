from django.db import models

# Refer to the documentation of Django Models
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()


