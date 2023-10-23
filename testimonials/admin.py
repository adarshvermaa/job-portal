from django.contrib import admin
from .models import PostCategory,PostSection,Testimonial
# Register your models here.


class PostSectionAdmin(admin.ModelAdmin):
    list_display = ("user","title","category",)
    search_fields=  ("user","title","category",)

admin.site.register(PostCategory)
admin.site.register(PostSection,PostSectionAdmin)
admin.site.register(Testimonial)