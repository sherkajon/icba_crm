from django.contrib import admin
from .models import Contact, Organization, Menu


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('Name','Category', 'Address', 'Website','Email','Phone')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Email','Phone_Number','designation', 'Organization')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'alt')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Menu, MenuAdmin)


# Register your models here.