from django import forms
from .models import NewQuestionModel


class Search(forms.Form):
    search = forms.CharField(max_length=200, required=True)

class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = NewQuestionModel
        fields = ['title', 'text']