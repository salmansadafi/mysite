from django import forms
from .models import Contact, Newsletter


class contactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'