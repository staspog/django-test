from django.http import HttpResponse
from django.shortcuts import render
from .forms import Search, NewQuestionForm


def main(request):
    searchform = Search() 
    return render(request, "main.html", {"search_form": searchform})

def new_question(request):
    if request.method == "POST":
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NewQuestionForm()
    return render(request, "new_question.html", {"form": form })