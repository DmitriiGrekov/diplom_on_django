from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20, label='Телефон')
    first_name = forms.CharField(max_length=20, label='Имя')
    last_name = forms.CharField(max_length=20, label='Фамилия')

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no',
                  'password1', 'password2', 'first_name', 'last_name']


User._meta.get_field('email')._unique = True


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'country', 'about', 'img')
        labels = {
            'date_of_birth': 'Дата Рождения',
            'country': 'Страна',
            'about': 'О вас',
            'img': 'Изображение профиля(введите ссылку)'
        }
