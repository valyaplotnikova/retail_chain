from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active', 'is_superuser', )
    list_filter = ('email', 'is_active')
    search_fields = ('email',)
    list_editable = ('is_active',)
    list_display_links = ('email',)
