from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from flashcards.models import Client
from .models import *

class partnerAdmin(admin.ModelAdmin):
    list_display=['name', 'timer']

class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'employee'

class UserAdmin(BaseUserAdmin):
    inlines = (ClientInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(partner)