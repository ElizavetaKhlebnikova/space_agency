from django.db import models
from filer.fields.image import FilerImageField


class ImageForMainPageModel(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name=u"Название картинки")
    image = FilerImageField(related_name='image', on_delete=models.CASCADE, null=True, blank=True, verbose_name=u"Картинка")
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name=u"Порядок отображения"
    )

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return f'Image ID: {self.image.id}, order: {self.my_order}'
