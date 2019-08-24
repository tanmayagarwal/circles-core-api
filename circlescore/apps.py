from django.apps import AppConfig


class CirclescoreConfig(AppConfig):
    name = 'circlescore'

    def ready(self):
        import circlescore.signals