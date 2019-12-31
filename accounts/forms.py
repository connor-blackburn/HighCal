from django import forms

class LoginForm(forms.Form):
    ''' User log in form '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

