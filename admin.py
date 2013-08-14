from django.contrib import admin
from django_media.models import MediaGallery, Media

class MediaInline(admin.TabularInline):
    model = MediaGallery.media.through
    extra = 0
    
    
class MediaGalleryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information',               {'fields': ['title', 'description']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('User information', {'fields': ['gallery_users', 'gallery_admins']}),
    ]
    inlines = [MediaInline]

admin.site.register(Media)
admin.site.register(MediaGallery, MediaGalleryAdmin)