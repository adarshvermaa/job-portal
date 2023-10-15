from django.contrib import admin
from .models import Resume,ProfileCompletionStar
from django.utils.text import Truncator
# Register your models here.


# def eductaion(obj):
#     name = "%s" % str(obj.eductaion.html)
#     return Truncator(name).chars(30)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('linkdin_profile','email','phone_number',)
    search_fields = ('linkdin_profile','email','phone_number',)


class ProfileCompletionStarAdmin(admin.ModelAdmin):
    list_display = ('resume','screening_test','video_test','community',)

admin.site.register(ProfileCompletionStar,ProfileCompletionStarAdmin)
admin.site.register(Resume,ResumeAdmin)