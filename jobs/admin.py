from django.contrib import admin
from .models import JobCategory,PostJob
# Register your models here.


class JobCategoryAdmin(admin.ModelAdmin):
    list_display= ('category','created_date','modified_date')
    search_fields = ('category',)



class PostJobAdmin(admin.ModelAdmin):
    list_display = ('job_title','last_date','company_name',)
    search_fields = ('job_title', 'company_name',)

admin.site.register(JobCategory,JobCategoryAdmin)
admin.site.register(PostJob,PostJobAdmin)