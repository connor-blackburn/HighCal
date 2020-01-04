from django.db import models
from django.utils import timezone

"""
Model for client reviews
"""
class Review(models.Model):
    job_title = models.CharField(max_length=200)
    review_title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="img", null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.job_title