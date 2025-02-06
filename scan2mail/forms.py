from django import forms
 
# creating a form 
class InputForm(forms.Form):
 
    to = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the recipient\'s email', 'id': 'to'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the email\'s subject', 'id': 'subject'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the email\'s text', 'id': 'body'}))
