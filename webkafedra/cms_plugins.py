from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import StaffGallery, ImageLinkPluginModel
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from cms.plugin_base import CMSPluginBase
from .models import Document
import feedparser


# Плагин для галереи сотрудников
class StaffGalleryPlugin(CMSPluginBase):
    model = StaffGallery
    name = _("Галерея сотрудников")
    render_template = "staff_gallery_plugin.html"  # шаблон лежит в корне templates
    allow_children = True  # Разрешаем вложенные плагины
    child_classes = ["ImageLinkPlugin"]  # Внутри могут быть только плагины с изображениями
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            "instance": instance,
            "placeholder": placeholder,
        })
        return context

plugin_pool.register_plugin(StaffGalleryPlugin)

# Плагин для картинки с текстовой ссылкой
class ImageLinkPlugin(CMSPluginBase):
    model = ImageLinkPluginModel
    name = _("Картинка с текстовой ссылкой")
    render_template = "image_link_plugin.html"  # шаблон лежит в корне templates
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            "instance": instance,
            "placeholder": placeholder,
        })
        return context

plugin_pool.register_plugin(ImageLinkPlugin)

# Плагин для отображения формы входа
class LoginFormPlugin(CMSPluginBase):
    name = _("Форма входа")
    render_template = "login_form_plugin.html"  # шаблон располагается в корне templates
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            "instance": instance,
            "form": AuthenticationForm(),
            "placeholder": placeholder,
        })
        return context

plugin_pool.register_plugin(LoginFormPlugin)

# Плагин для отображения формы регистрации
class RegistrationFormPlugin(CMSPluginBase):
    name = _("Форма регистрации")
    render_template = "registration_form_plugin.html"  # шаблон в корне templates
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            "instance": instance,
            "form": UserCreationForm(),
            "placeholder": placeholder,
        })
        return context

plugin_pool.register_plugin(RegistrationFormPlugin)

# Плагин для отображения кнопки выхода
class LogoutButtonPlugin(CMSPluginBase):
    name = _("Кнопка выхода")
    render_template = "logout_button_plugin.html"  # шаблон в корне templates
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            "instance": instance,
            "logout_url": "/logout/",  # Можно заменить на reverse("logout")
            "placeholder": placeholder,
        })
        return context

plugin_pool.register_plugin(LogoutButtonPlugin)


class DocumentCMSPlugin(CMSPluginBase):
    name = _("Документы")  # Это имя будет отображаться в списке плагинов
    render_template = "document_plugin.html"  # путь к шаблону плагина
    cache = False  # отключаем кэширование, если данные динамические

    def render(self, context, instance, placeholder):
        documents = Document.objects.all().order_by('-uploaded_at')
        context.update({
            'documents': documents,
            # Можно добавить дополнительные переменные, например, instance, placeholder и т.д.
            'placeholder': placeholder,
            'instance': instance,
        })
        return context
plugin_pool.register_plugin(DocumentCMSPlugin)



class RSSNewsPlugin(CMSPluginBase):
    name = _("Новости (RSS)")
    render_template = "rss_news_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        rss_url = "https://tproger.ru/feed"
        feed = feedparser.parse(rss_url)

        news_items = [{
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary
        } for entry in feed.entries[:15]]

        context.update({
            'news_items': news_items,
            'placeholder': placeholder,
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(RSSNewsPlugin)