from django.contrib import admin
from django.core.mail import EmailMessage
from django.conf import settings
# Register your models here.

from .models import *

@admin.register(UserData)
class MaleUserDataAdmin(admin.ModelAdmin):
    list_display = ['CID','Name', 'email', 'Village', 'Chiwog', 'HouseHoldNo', 'contact_number', 'status']
    search_fields = ['CID']
    actions = ['make_published']
    
    def make_published(self, request, queryset):
        queryset.update(status=True)
        for obj in queryset:
            print("Hello", obj.email)
            email1 = EmailMessage(
                "Gewog Management System",
                "Hello " + obj.Name + " we have berified your data,  You have successfully added your data to system.",
                settings.EMAIL_HOST_USER,
                [obj.email]
                )
            email1.fail_silently = False
            email1.send()

@admin.register(Marriage)
class MarriageUserDataAdmin(admin.ModelAdmin):
    list_display = ['MarriageId','user', 'Spousecid', 'MarriageCertificate', 'status']
    search_fields = ['YOUR_CId']
    actions = ['make_published']
    def make_published(self, request, queryset):
        queryset.update(status=True)
        for obj in queryset:
            # print("Hello", obj.YOUR_CId.email)
            email1 = EmailMessage(
                "Gewog Management System",
                "Hello " + str(obj.user) + " we have verified your data and you have successfully added your marriage data to our system",
                settings.EMAIL_HOST_USER,
                [obj.user.email]
                )
            email1.fail_silently = False
            email1.send()


@admin.register(Passdata)
class PassDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'reason', 'request_date', 'status']
    search_fields = ['user']
    actions = ['Accept', 'Reject']
    def Accept(self, request, queryset):
        queryset.update(status='Accepted')
        # for obj in queryset:
        #     print("Hello", obj.YOUR_CId.email)
        #     email1 = EmailMessage(
        #         "Gewog Management System",
        #         "Hello " + str(obj.user) + " we have verified your data and you have successfully added your marriage data to our system",
        #         settings.EMAIL_HOST_USER,
        #         [obj.email]
        #         )
        #     email1.fail_silently = False
        #     email1.send()

    def Reject(self, request, queryset):
        queryset.update(status='Rejected')
        # for obj in queryset:
        #     # print("Hello", obj.YOUR_CId.email)
        #     email1 = EmailMessage(
        #         "Gewog Management System",
        #         "Hello " + str(obj.user) + " we have verified your data and you have successfully added your marriage data to our system",
        #         settings.EMAIL_HOST_USER,
        #         [obj.email]
        #         )
        #     email1.fail_silently = False
        #     email1.send()

admin.site.register(childdata)

admin.site.register(Annoucement)