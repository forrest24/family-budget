from django.contrib import admin
from django.contrib.auth.models import Group

from apps.users.models import CustomUser

admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    fields = (
        "first_name",
        "last_name",
        "slug",
        "email",
        "password",
        "is_staff",
        "is_active",
        "user_permissions",
    )
