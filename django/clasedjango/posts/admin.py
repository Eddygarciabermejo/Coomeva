from django.contrib import admin

# Register your models here.

from posts.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'website','phone_number','picture')
    list_display_links = ('pk','user')
    list_editable=('website','phone_number','picture')
    search_fields= ('user__email','user__first_name', 'user__last_name','phone_number')