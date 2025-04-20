from django.db import models
from cms.models.pluginmodel import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField

class ImageLinkPluginModel(CMSPlugin):
    """
    Модель для плагина "Картинка с текстовой ссылкой"
    """
    image = FilerImageField(
        verbose_name='Изображение',
        on_delete=models.CASCADE,
        related_name='image_link_images',
        help_text='Загрузите вертикальное изображение'
    )
    text = HTMLField(
        'Текст ссылки',
        help_text='Текст, который будет отображаться как ссылка'
    )
    url = models.CharField(
        'URL ссылки',
        max_length=255,
        help_text='Введите URL, на который будет вести ссылка'
    )
    
    def __str__(self):
        return self.text or f"Ссылка #{self.id}"