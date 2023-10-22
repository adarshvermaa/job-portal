from rest_framework.serializers import  ModelSerializer
from .models import AppliedJobs
from jobs.serializers import PostJobSerializers
from resume.serializers import ResumeSerializers

class AppliedJobsSerializers(ModelSerializer):
    class Meta:
        model = AppliedJobs
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['postjob'] = PostJobSerializers(instance.postjob).data
        response['resume'] = ResumeSerializers(instance.resume).data
        return response