from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'your name'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Leave a comment'}))
