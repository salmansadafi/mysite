from django import forms
from .models import Comment
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('approved',)