from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(UserCreationForm):
    token = forms.CharField(max_length=200)
    class Meta:
        model = User
        fields = ('username', 'token', 'password1', 'password2', )

class IdForm(forms.Form):
    id = forms.CharField(label='Ид')

class MessageForm(forms.Form):
    id = forms.CharField(label='id пользователя или группы')
    msg = forms.CharField(label='Текст сообщения',widget=forms.Textarea)

class InviteForm(forms.Form):
    id = forms.CharField(label='Ваш id или группы')
    id_group = forms.CharField(label='id группы для раскрутки')