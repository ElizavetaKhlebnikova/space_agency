from django.contrib import admin
from .models import ImageForMainPageModel
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin


@admin.register(ImageForMainPageModel)
class ImageForMainPageModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'image_preview')

    @admin.display(description="предварительный просмотр изображения")
    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="100px" height="100px">'.format(obj.image.url))
        return 'нет изображения'

    image_preview.allow_tags = True
