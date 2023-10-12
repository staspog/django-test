from django.urls import path
from hello.views import main, new_question

urlpatterns = [
        path('', main, name = 'main'),
        path('new_question', new_question, name = 'new_question')
]