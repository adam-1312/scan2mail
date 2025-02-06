from django import forms
 
# creating a form 
class InputForm(forms.Form):
 
    to = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the recipients\' emails separated by commas', 'id': 'to'}))
    cc = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the emails separated by commas', 'id': 'cc'}))
    bcc = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the emails separated by commas', 'id': 'bcc'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the email\'s subject', 'id': 'subject'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the email\'s text', 'id': 'body'}))
    api_key = forms.CharField(label='API Key (tinyurl)', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Paste your tinyurl API key', 'id': 'api_key'}))
    alias = forms.CharField(label='Alias (tinyurl)', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phrase to use as tinyurl alias', 'id': 'alias'}))
