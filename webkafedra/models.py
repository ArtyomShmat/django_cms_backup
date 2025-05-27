from django.db import models
from cms.models.pluginmodel import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from django.contrib.auth.models import User

class StaffGallery(CMSPlugin):
    title = models.CharField("Заголовок", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title or "Галерея сотрудников"

class ImageLinkPluginModel(CMSPlugin):
    """
    Модель для плагина "Картинка с текстовой ссылкой"
    """
    image = FilerImageField(
        verbose_name='Изображение',
        on_delete=models.CASCADE,
        related_name='image_link_images',
        help_text='Загрузите изображение'
    )
    text = HTMLField(
        'Текст ссылки',
        help_text='Введите текст ссылки'
    )
    url = models.URLField(
        'URL ссылки',
        max_length=255,
        help_text='Введите URL, на который будет вести ссылка'
    )

    def __str__(self):
        return self.text or f"Ссылка #{self.pk}"
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    access_level = models.CharField(max_length=50, blank=True, null=True)  # Редактирует только администратор

    def __str__(self):
        return self.user.username
    




class Document(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название документа")
    file = models.FileField(upload_to='documents/', verbose_name="Файл")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")
    # Указываем, кто загрузил документ (будет заполняться только в случае суперпользователя)
    uploaded_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="Загружено суперпользователем"
    )

    def __str__(self):
        return self.title
