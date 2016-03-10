from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
import re

CORRECT_REGEX = re.compile(r'^[A-Za-z0-9_]+$')
CORRECT_NAME_REGEX = re.compile(r'^[А-ЯЁ][а-яё]*$')


class ExtendedUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label=_('first name'), required=True)
    last_name = forms.CharField(label=_('last name'), required=True)
    email = forms.EmailField(label=_('Email'), required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and len(username) < 3:
            raise forms.ValidationError('Имя пользователя должно быть не короче 3-х символов')
        if username and not CORRECT_REGEX.match(username):
            raise forms.ValidationError('Имя пользователя должно создержать только цифры,'
                                        ' латинские буквы или знак нижнего подчёркивания')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and not CORRECT_REGEX.match(password):
            raise forms.ValidationError('Пароль должен создержать только цифры,'
                                        ' латинские буквы или знак нижнего подчёркивания')
        return password

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and len(first_name) < 2:
            raise forms.ValidationError('Имя должно быть не короче 2-х символов')
        if first_name and not CORRECT_NAME_REGEX.match(first_name):
            raise forms.ValidationError('Имя должно начинаться с заглавной буквы и содержать только буквы')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name and len(last_name) < 2:
            raise forms.ValidationError('Фамилия должна быть не короче 2-х символов')
        if last_name and not CORRECT_NAME_REGEX.match(last_name):
            raise forms.ValidationError('Фамилия должна начинаться с заглавной буквы и содержать только буквы')
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError('Даный адрес уже используется')
        return email

    def save(self, commit=True):
        user = super(ExtendedUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
