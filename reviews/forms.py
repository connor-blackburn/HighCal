from django import forms
from .models import Review

class ClientReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('job_title', 'review_title', 'description', 'published_date')