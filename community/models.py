from django.db import models
from account.models import BaseModel,User
from tinymce.models import HTMLField
# Create your models here.

class CommunityParticipation(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    title = models.CharField(max_length=100)
    description = HTMLField(blank=True,null=True)

class CommunityReviews(models.Model):
    community = models.ForeignKey(CommunityParticipation,models.CASCADE)
    comment = models.TextField()
    
