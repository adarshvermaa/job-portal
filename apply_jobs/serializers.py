from rest_framework.serializers import  ModelSerializer
from .models import AppliedJobs
from jobs.serializers import PostJobSerializers
from resume.serializers import ResumeSerializers
from resume.serializers import ProfileCompletionStar

class AppliedJobsSerializers(ModelSerializer):
    class Meta:
        model = AppliedJobs
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['postjob'] = PostJobSerializers(instance.postjob).data
        response['resume'] = ResumeSerializers(instance.resume).data
        return response
    
    def create(self, validated_data):
        resume = super().create(validated_data)

        # Set the related profileCompletionStar resume field to True
        profile_star, created = ProfileCompletionStar.objects.get_or_create()
        profile_star.resume = True
        profile_star.save()

        return resume