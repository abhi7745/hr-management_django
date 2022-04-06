from django.contrib import admin

from accounts.models import Extend_usermodel
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import *


# Register your models here.

class UserInline(admin.StackedInline):
    model=Extend_usermodel
    can_delete=False
    verbose_name_plural='Extend_usermodel'

class CustomizedUserAdmin(UserAdmin):
    inlines=(UserInline,)

admin.site.unregister(User)

admin.site.register(User,CustomizedUserAdmin)

# admin.site.register(Recruiter)
# admin.site.register(Candidate)
