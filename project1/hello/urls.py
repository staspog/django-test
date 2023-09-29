from django.urls import path
from hello.views import index, about

urlpatterns = [
        path('', index, name = 'home'),
        path('about/', about, name = 'about')
]