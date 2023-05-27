from django import forms
from .models import *


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'text_comments')


class SubscriberForm(forms.Form):
    email = forms.EmailField(label="Email", required=True, widget=forms.widgets.EmailInput(
        attrs={'type': 'email', 'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'name@example.com'}))

    class Meta:
        model = Subscriber
        exclude = ['']


class OrderForm(forms.Form):
    name = forms.CharField(label='ФИО', max_length=50,
                           widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО*'}))
    phone = forms.CharField(max_length=13, required=True,
                            widget=forms.widgets.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Телефон*'}))
    email = forms.EmailField(label='Email',
                             widget=forms.widgets.TextInput(
                                 attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email'}))

    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'details', 'data']
