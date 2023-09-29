from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World')

def about(request):
    return HttpResponse('<h1> About our app </h1>')