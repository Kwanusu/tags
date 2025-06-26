from django import forms
from .models import Subscriber, Blog, Author

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        
class BlogForm(forms.ModelForm):
# Define the author field as a dropdown menu of authors
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Select an author")
        
class Meta:
    model = Blog
    fields = ['author', 'title', 'content', 'is_published']

def __init__(self, *args, **kwargs):
    super(BlogForm, self).__init__(*args, **kwargs)
    # Customize the form's appearance or behavior here if needed

def clean(self):
    cleaned_data = super().clean()
    # Additional form validation can be performed here
    return cleaned_data