# В файле forms.py вашего приложения

from django import forms
from .models import UserProfile
from .models import Document

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # Поля, которые пользователь может редактировать;
        # если пользователь не админ, то поле access_level не выводим.
        fields = ['photo', 'description', 'access_level']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # ожидаем передачу пользователя при инициализации
        super().__init__(*args, **kwargs)
        if not (user and user.is_superuser):
            # Если текущий пользователь не является администратором, убираем поле access_level,
            # чтобы предотвратить его изменение.
            self.fields.pop('access_level', None)


class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file', 'description']