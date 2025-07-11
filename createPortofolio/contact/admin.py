from django.contrib import admin
from .models import ContactSection, Sosmed
from unfold.admin import ModelAdmin
from django.utils.html import format_html

class ContactSectionAdmin(ModelAdmin):
    list_display = ('title', 'content', 'thumbnail')
    search_fields = ('title', 'content')

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;"/>', obj.image.url)
        return 'No Image'
    thumbnail.short_description = 'Image'

class SosmedAdmin(ModelAdmin):
    list_display = ('name', 'icon', 'link', 'icon_display')
    search_fields = ('icon', 'link')

    def icon_display(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="width: 30px; height: 30px;"/>', obj.icon.url)
        return 'No Icon'
    icon_display.short_description = 'Icon'

admin.site.register(ContactSection, ContactSectionAdmin)
admin.site.register(Sosmed, SosmedAdmin)
