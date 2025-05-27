from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.contrib.auth import views as auth_views
from webkafedra.views import RegisterView, dashboard, document_list, document_upload, document_delete

admin.autodiscover()

urlpatterns = [
    # Карта сайта
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    
    # Регистрация и стандартные URL-аутентификации
    path("accounts/register/", RegisterView.as_view(), name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    
    # Личный кабинет
    path("dashboard/", dashboard, name="dashboard"),
    
    # Документы: список, загрузка и удаление (удаление доступно только суперпользователю)
    path("documents/", document_list, name="document_list"),
    path("documents/upload/", document_upload, name="document_upload"),
    path("documents/delete/<int:pk>/", document_delete, name="document_delete"),
]

# Подключаем админку и Django CMS с поддержкой i18n.
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("cms.urls")),  # пустой путь – домашняя страница CMS
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
