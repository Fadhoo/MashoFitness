from django.apps import AppConfig


class ThemeConfig(AppConfig):
    name = 'theme'

    def ready(self):
        from .gym_scheduler import smsGymScheduler
        print('scheduler start ......')
        smsGymScheduler.start_scheduler()