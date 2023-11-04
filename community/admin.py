from django.contrib import admin
from .models import CommunityParticipation,CommunityReviews
# Register your models here.

class CommunityParticipationAdmin(admin.ModelAdmin):
    list_display=('user','title')
    search_fields= ('user','title')

admin.site.register(CommunityReviews)
admin.site.register(CommunityParticipation,CommunityParticipationAdmin)
