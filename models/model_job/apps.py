from django.apps import AppConfig


class ModelJobConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'models.model_job'
    verbose_name = 'jobs'
