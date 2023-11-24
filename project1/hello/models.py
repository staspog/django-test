from django.db import models

class NewQuestionModel(models.Model):
    title = models.CharField("Заголовок", max_length=75, blank=False)
    text = models.CharField("Текст/Комментарий", max_length=1000, blank=False)
