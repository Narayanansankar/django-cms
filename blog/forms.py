from django import forms
from blog.models import BlogPost
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 10:
            raise ValidationError("The title must be at least 10 characters long.")
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(strip_tags(content)) < 50:
            raise ValidationError("Meaningful content is required (at least 50 characters).")
        return content