from django.contrib import admin
from .models import Resume,ProfileCompletionStar
# Register your models here.


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('linkdin_profile','email','phone_number',)
    search_fields = ('linkdin_profile','email','phone_number',)


class ProfileCompletionStarAdmin(admin.ModelAdmin):
    list_display = ('resume','screening_test','video_test','community',)

admin.site.register(ProfileCompletionStar,ProfileCompletionStarAdmin)
admin.site.register(Resume,ResumeAdmin)