from django.contrib import admin
from .models import HomepageContent, AboutInfo, Service, Program, ContactMessage

admin.site.register(HomepageContent)
admin.site.register(AboutInfo)
admin.site.register(Service)
admin.site.register(Program)
admin.site.register(ContactMessage)
