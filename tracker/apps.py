from django.apps import AppConfig


class TrackerConfig(AppConfig):
    name = 'tracker'

    def ready(self):
        from . import signals
