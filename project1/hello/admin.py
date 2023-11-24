from django.contrib import admin
from .models import NewQuestionModel

class NewQuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(NewQuestionModel, NewQuestionAdmin)