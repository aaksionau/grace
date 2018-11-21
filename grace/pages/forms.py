from django import forms
from .models import Feedback

class ContactsForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}), label='Ваш email')
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}), label='Ваше имя')
    body = forms.CharField( widget=forms.Textarea(attrs={'rows': 10, 'cols': 40, 'class' : 'form-control'}), label='Ваше сообщение')

    class Meta:
        model = Feedback
        fields = '__all__'
