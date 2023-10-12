from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return render(request, "main.html")

def new_question(request):
    return render(request, "new_question.html")

def about(request):
    return HttpResponse('<h1> About our app </h1>')