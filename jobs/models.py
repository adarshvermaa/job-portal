from django.db import models
from account.models import BaseModel
# Create your models here.

class JobCategory(BaseModel):
    category = models.CharField(max_length=100)
    def  __str__(self):
        return self.category

class PostJob(BaseModel):
    job_category = models.ForeignKey(JobCategory,on_delete=models.CASCADE,help_text="please select the job category", related_name="job_category")
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField()
    job_title = models.CharField(max_length=100)
    last_date = models.DateTimeField(auto_now=True,help_text="Enter last date and time for jobs")
    skills = models.CharField(max_length=200,blank=True)
    description = models.TextField(blank=True)
    
    



