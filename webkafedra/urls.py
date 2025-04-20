from cms.sitemaps import CMSSitemap 
from django.conf import settings 
from django.conf.urls.i18n import i18n_patterns 
from django.conf.urls.static import static 
from django.contrib import admin 
from django.contrib.sitemaps.views import sitemap 
from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import RegisterView  # Импортируйте ваш вью для регистрации

admin.autodiscover() 

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path('accounts/register/', RegisterView.as_view(), name='register'),  # Новый маршрут для регистрации
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # другие пути аутентификации, если есть
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("cms.urls")),
    # другие пути вашего приложения
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.urls import path
from . import views  # Импортируйте ваши вью


