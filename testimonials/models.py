from django.db import models
from account.models import BaseModel,User
from tinymce.models import HTMLField

class Testimonial(BaseModel):
    pass

class PostCategory(BaseModel):
    user = models.ForeignKey(User,models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=100)

class PostSection(BaseModel):
    user = models.ForeignKey(User,models.CASCADE)
    category = models.ForeignKey(PostCategory,models.CASCADE)
    title = models.CharField(max_length=100)
    description = HTMLField(blank=True,null=True)

