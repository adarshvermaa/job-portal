from django.db import models
from account.models import BaseModel,User
# Create your models here.


class Resume(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    