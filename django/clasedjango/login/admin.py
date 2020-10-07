from django.contrib import admin

# Register your models here.

from login.models import Publicacion

@admin.register(Publicacion)
class PublicsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'photo', 'tittle')
    list_display_links = ('pk','user')
    list_editable= ('photo','tittle')
    search_fields= ('created', 'modified')