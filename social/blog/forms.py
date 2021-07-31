from django import forms
from django.forms.widgets import Widget
from .models import Post

class NewPostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':50,'style':'resize:none;','placeholder':'Type new post here' }), label='Content')
    event = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'cols':20,'style':'resize:none;','placeholder':'Type the event here' }), label='Event')
    date = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'cols':20,'style':'resize:none;','placeholder':'Type the date of the event here' }), label='Date')
    place = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'cols':20,'style':'resize:none;','placeholder':'Type the setting of the event here' }), label='Location')
     
    class Meta:
        model = Post
        fields = ['content', 'event', 'date', 'place']
