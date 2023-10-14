from django.db import models
from account.models import BaseModel,User
from django_quill.fields import QuillField
# Create your models here.


class Resume(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ImageField(blank=True,null=True)
    linkdin_profile = models.URLField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    phone_number = models.IntegerField(blank=True,null=True)
    eductaion = QuillField(blank=True,null=True)
    skills = models.CharField(max_length=1000,blank=True,null=True)
    projects = QuillField(blank=True,null=True)
    extra_circulam_activity = QuillField(blank=True,null=True)
    achivements = QuillField(blank=True,null=True)


class ProfileCompletionStar(BaseModel):
    resume = models.BooleanField(default=False)
    screening_test = models.BooleanField(default=False)
    video_test = models.BooleanField(default=False)
    community = models.BooleanField(default=False)
    
    