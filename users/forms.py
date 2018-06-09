from django import forms
from django.contrib.auth import password_validation

from users.models import User


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'class_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                '이미 가입된 이메일 입니다.'
            )
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError(
                '이미 가입된 휴대폰 번호 입니다.'
            )
        return phone_number

    def clean_class_number(self):
        class_number = self.cleaned_data['class_number']
        if User.objects.filter(class_number=class_number).exists():
            raise forms.ValidationError(
                '이미 가입된 학번 입니다.'
            )
        return class_number

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                '비밀번호 확인이 일치하지 않습니다.'
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
