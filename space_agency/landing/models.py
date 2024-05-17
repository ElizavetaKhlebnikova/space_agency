from django.db import models
from filer.fields.image import FilerImageField


class ImageForMainPageModel(models.Model):
    name = models.CharField(max_length=255, default='')
    image = FilerImageField(related_name='изображение', on_delete=models.CASCADE, null=True, blank=True)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f'Image ID: {self.image.id}, order: {self.my_order}'
