from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

from .models import User, Item

#admin.site.register(User)
admin.site.register(Item)
admin.site.register(CustomUser, UserAdmin)


