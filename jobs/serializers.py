from rest_framework.serializers import  ModelSerializer
from .models import JobCategory,PostJob
from django.contrib.sites.shortcuts import get_current_site


class JobCategorySerializers(ModelSerializer):
    class Meta:
        model = JobCategory
        exclude = ['created_date','modified_date']


class PostJobSerializers(ModelSerializer):
    job_category = JobCategorySerializers() # nested  Serializers
    class Meta:
        model = PostJob
        fields = "__all__"
    def company_logoImage(self, obj):
        return self.build_absolute_image_url(obj.company_logo)
    

    def build_absolute_image_url(self, image_path):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(image_path)
        else:
            # If request is not available (for example, in shell), use the default site
            site = get_current_site(None)
            return f"{site.scheme}://{site.domain}{image_path}"