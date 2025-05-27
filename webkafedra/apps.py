from django.apps import AppConfig

class WebkafedraConfig(AppConfig):
    name = 'webkafedra'

    def ready(self):
        # Импорт сигналов производится здесь, когда приложения уже загружены
        import webkafedra.signals
