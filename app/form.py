# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email Address',required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=20, required=True, label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Message',required=True)
