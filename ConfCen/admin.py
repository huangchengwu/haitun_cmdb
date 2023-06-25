from django.contrib import admin
from .models import *
from django.shortcuts import render,HttpResponse

# Register your models here.

admin.site.site_title = "海豚运维管理系统"
admin.site.site_header = "海豚运维管理系统"


# @admin.register(Host)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('hostname','internal_ip_address','external_ip_address','ssh_username','os_version')
#     search_fields = ('hostname','internal_ip_address','external_ip_address','os_version')

admin.site.register([k8sPm])