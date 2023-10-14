from rest_framework.serializers import  ModelSerializer
from .models import Resume, ProfileCompletionStar
from django.contrib.sites.shortcuts import get_current_site
# from django_quill.serializers import QuillSerializerMixin


class ProfileCompletionStarSerializers(ModelSerializer):
    class Meta:
        models = ProfileCompletionStar
        fields = "__all__"

class ResumeSerializers(ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"

    def pictureImage(self, obj):
        return self.build_absolute_image_url(obj.picture)
    

    def build_absolute_image_url(self, image_path):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(image_path)
        else:
            # If request is not available (for example, in shell), use the default site
            site = get_current_site(None)
            return f"{site.scheme}://{site.domain}{image_path}"
        

    def create(self, validated_data):
        resume = super().create(validated_data)

        # Set the related profileCompletionStar resume field to True
        profile_star, created = ProfileCompletionStar.objects.get_or_create()
        profile_star.resume = True
        profile_star.save()

        return resume
        



