from django.contrib import admin
from .models import Job

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        ('图片 (Image)', {'fields': ['image']}),
        ('小节 (Summary)', {'fields': ['summary']}),
    ]

admin.site.register(Job, JobAdmin)
