from django.contrib import admin
from .models import ImageForMainPageModel
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
from easy_thumbnails.files import get_thumbnailer
from django.utils.html import format_html


@admin.register(ImageForMainPageModel)
class ImageForMainPageModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'thumbnail')

    def thumbnail(self, obj):
        if obj.image:
            thumbnail_url = get_thumbnailer(obj.image).get_thumbnail({
                'size': (0, 100),
                'crop': True,
                'upscale': True,
            }).url
            return format_html('<img src="{}" alt="Thumbnail">', thumbnail_url)
        return "No Image"

    thumbnail.short_description = "предварительный просмотр изображения"
