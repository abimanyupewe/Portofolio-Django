from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import BlogSection, Category, ExperienceSection, Framework, HeroSection, LanguageProgramming, ProjectSection, SkillSection, Stack, Status
from django.utils.html import format_html

# Register your models here.

class HeroSectionAdmin(ModelAdmin):
    list_display = ('title', 'span', 'experience', 'available_for_work', 'working_on', 'custom_text', 'category', 'thumbnail')
    search_fields = ('title', 'span')

    def thumbnail(self, obj):
        if obj.imageProfile:
            return format_html('<img src="{}" style="width: 50px; height: auto;"/>'.format(obj.imageProfile.url))
        else:
            return 'No Image'
    thumbnail.short_description = 'Image'

class CategoryAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
class SkillSectionAdmin(ModelAdmin):
    list_display = ('title', 'description', 'thumbnail')
    search_fields = ('title',)

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;"/>'.format(obj.image.url))
        else:
            return 'No Image'
    thumbnail.short_description = 'Image'

class ExperienceSectionAdmin(ModelAdmin):
    list_display = ('company', 'position', 'location', 'category', 'start_date', 'end_date', 'currently_working', 'thumbnail')
    search_fields = ('company', 'position', 'location', 'category__name')

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;"/>'.format(obj.image.url))
        else:
            return 'No Image'
    thumbnail.short_description = 'Image'

class ProjectSectionAdmin(ModelAdmin):
    list_display = ('title', 'description', 'textBtn', 'link', 'stack', 'category', 'language', 'framework', 'status', 'thumbnail')
    search_fields = ('title','description')
    list_filter = ('language', 'framework', 'stack', 'category', 'status')
    list_per_page = 4

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;"/>'.format(obj.image.url))
        else:
            return 'No Image'
    thumbnail.short_description = 'Image'

class LanguageProgrammingAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class FrameworkAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class StatusAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class StackAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class BlogSectionAdmin(ModelAdmin):
    list_display = ('title', 'author', 'published', 'category', 'thumbnail')
    search_fields = ('title', 'author')
    list_filter = ('published', 'category')
    prepopulated_fields = {'slug': ('title',)}

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;"/>'.format(obj.image.url))
        else:
            return 'No Image'
    thumbnail.short_description = 'Image'

admin.site.register(HeroSection, HeroSectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SkillSection, SkillSectionAdmin)
admin.site.register(ExperienceSection, ExperienceSectionAdmin)
admin.site.register(ProjectSection, ProjectSectionAdmin)
admin.site.register(LanguageProgramming, LanguageProgrammingAdmin)
admin.site.register(BlogSection, BlogSectionAdmin)
admin.site.register(Framework, FrameworkAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Stack, StackAdmin)