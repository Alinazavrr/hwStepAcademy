from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Ad(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField()
    img = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)