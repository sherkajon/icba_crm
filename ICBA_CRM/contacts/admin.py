from django.contrib import admin
from .models import Contact, Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('Name','Category', 'Address', 'Website','Email','Phone')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Email','Phone_Number','designation', 'Organization')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Organization, OrganizationAdmin)


# Register your models here.