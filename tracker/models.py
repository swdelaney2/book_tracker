from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    google_id = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField()

    def __str__(self):
        return self.title
