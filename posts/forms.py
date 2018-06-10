from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post


class PostForm(forms.ModelForm):
    type = forms.HiddenInput()

    class Meta:
        model = Post
        fields = ('title', 'content', 'type')
        widgets = {
            'content': SummernoteWidget(),
        }

