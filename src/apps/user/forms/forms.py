from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Обязательно.', label='Имя')
    last_name = forms.CharField(max_length=30, required=True, help_text='Обязательно.', label='Фамилия')
    patronymic = forms.CharField(max_length=30, required=True, help_text='Обязательно.', label='Отчество')
    email = forms.EmailField(max_length=254, help_text='Обязательно. Введите валидную почту.')
    passport_series = forms.CharField(max_length=2, required=True, label='Серия паспорта')
    passport_number = forms.CharField(max_length=7, required=True, label='Номер паспорта')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'patronymic',
            'email',
            'passport_series',
            'passport_number',
            'password1',
            'password2',
        )

    def get_full_name(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronymic
