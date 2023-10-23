from rest_framework.serializers import  ModelSerializer
from .models import PostSection,PostCategory

class PostSectionSerializers(ModelSerializer):
    class Meta:
        model = PostSection
        fields = "__all__"



class PostCategorySerializers(ModelSerializer):
    class Meta:
        model = PostCategory
        fields = "__all__"
