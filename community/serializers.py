from rest_framework.serializers import  ModelSerializer
from .models import CommunityParticipation,CommunityReviews
from resume.models import ProfileCompletionStar

class CommunityParticipationserializers(ModelSerializer):
    class Meta:
        model = CommunityParticipation
        fields = "__all__"
    def create(self, validated_data):
        resume = super().create(validated_data)

        # Set the related profileCompletionStar resume field to True
        profile_star, created = ProfileCompletionStar.objects.get_or_create()
        profile_star.resume = True
        profile_star.save()

        return resume

class CommunityReviewsserializers(ModelSerializer):
    class Meta:
        model = CommunityReviews
        fields = "__all__"