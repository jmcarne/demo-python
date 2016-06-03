from django import forms


class Login(forms.Form):
    user_name = forms.CharField(max_length=8)
    password = forms.CharField(max_length=8,widget=forms.PasswordInput)
    email = forms.EmailField(max_length=30,widget=forms.EmailInput)
    submit = forms
