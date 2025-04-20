from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

# Плагин для отображения формы входа
class LoginFormPlugin(CMSPluginBase):
    name = _("Форма входа")  # Название плагина в интерфейсе CMS
    render_template = "login_form_plugin.html"  # Шаблон плагина

    def render(self, context, instance, placeholder):
        # Передаём форму входа в шаблон
        context['form'] = AuthenticationForm()
        return context

# Регистрация плагина
plugin_pool.register_plugin(LoginFormPlugin)

from django.contrib.auth.forms import UserCreationForm

# Плагин для отображения формы регистрации
class RegistrationFormPlugin(CMSPluginBase):
    name = _("Форма регистрации")  # Название плагина в интерфейсе CMS
    render_template = "registration_form_plugin.html"  # Шаблон плагина

    def render(self, context, instance, placeholder):
        # Передаём форму регистрации в шаблон
        context['form'] = UserCreationForm()
        return context

# Регистрация плагина
plugin_pool.register_plugin(RegistrationFormPlugin)

# Плагин для отображения кнопки выхода
class LogoutButtonPlugin(CMSPluginBase):
    name = _("Кнопка выхода")  # Название плагина в интерфейсе CMS
    render_template = "logout_button_plugin.html"  # Шаблон плагина

    def render(self, context, instance, placeholder):
        return context

# Регистрация плагина
plugin_pool.register_plugin(LogoutButtonPlugin)