from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserSignupForm

# Register your models here.

from .models import Item

admin.site.register(Item)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserSignupForm
    form = CustomUserChangeForm
    
    list_display = ('email', 'is_staff', 'is_active', 'date_of_birth', 'profilePicture')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)