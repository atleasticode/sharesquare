from django.apps import AppConfig


class BenutzerConfig(AppConfig):
    name = 'benutzer'

    def ready(self):
        import benutzer.signals
