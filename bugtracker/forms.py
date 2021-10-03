from django import forms
from django.db.models.fields import TextField
from django.forms.widgets import Textarea
from bugtracker.models import Author


class TicketForm(forms.Form):
    title = forms.CharField(max_length=30)
    body = forms.CharField(widget=Textarea)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())


class TicketEdit(forms.Form):
    title = forms.CharField(max_length=30)
    body = forms.CharField(widget=Textarea)


class AuthorEdit(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
