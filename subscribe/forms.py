from django import forms
from django.contrib.auth.models import User

class Subscribe(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

    def __str__(self):
        return self.email