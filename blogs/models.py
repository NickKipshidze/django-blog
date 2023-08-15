from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=64)
    thumbnail = models.ImageField(upload_to="media/")
