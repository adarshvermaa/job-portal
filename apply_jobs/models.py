from django.db import models
from account.models import BaseModel
from resume.models import Resume
from jobs.models import PostJob
# Create your models here.


class AppliedJobs(BaseModel):
    resume = models.ForeignKey(Resume,models.CASCADE)
    postjob = models.ForeignKey(PostJob,models.CASCADE)
