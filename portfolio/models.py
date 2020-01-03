from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=250, default='')
    link = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title 

