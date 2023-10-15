from rest_framework.serializers import  ModelSerializer
from .models import Resume, ProfileCompletionStar
from django.contrib.sites.shortcuts import get_current_site
# from django_quill.serializers import QuillSerializerMixin
from django_quill.fields import QuillField

from rest_framework import serializers
import bleach
from bleach.linkifier import LinkifyFilter


class ProfileCompletionStarSerializers(ModelSerializer):
    class Meta:
        models = ProfileCompletionStar
        fields = "__all__"


class FieldQuill:
    def __init__(self, content):
        self.content = content

    def get_text_content(self):
        return "Extracted text content"
    def __str__(self):
        return f"FieldQuill(content={self.content})"

class QuillFieldSerializer(serializers.Field):
    def to_representation(self, value):
        # Assuming QuillField has a 'content' attribute
        return bleach.clean(value)

    def to_internal_value(self, data):
        # Handle conversion from JSON to QuillField instance if needed
        # This might involve creating a new QuillField instance with the provided content
        return QuillField(content=data)
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
        



