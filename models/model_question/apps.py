from django.apps import AppConfig


class ModelQuestionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'models.model_question'
    verbose_name = 'questions'
