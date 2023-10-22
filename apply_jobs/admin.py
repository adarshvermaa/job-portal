from django.contrib import admin
from .models import AppliedJobs
# Register your models here.

class AppliedJobsAdmin(admin.ModelAdmin):
    list_display= ('resume_user_email','created_date','modified_date','postjob_company_name')
    search_fields = ('resume_user_email','postjob_company_name',)
    def resume_user_email(self, obj):
        return obj.resume.user.email

    def postjob_company_name(self, obj):
        return obj.postjob.company_name

    resume_user_email.short_description = 'User Email'
    postjob_company_name.short_description = 'Company Name'


admin.site.register(AppliedJobs,AppliedJobsAdmin)
