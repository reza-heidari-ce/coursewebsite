from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise forms.ValidationError("کاربری با این نام کاربری وجود دارد")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("رمز عبور تکرار شده مطابقت ندارد")
        return password2


class ContactUsForm(forms.Form):
    subject = forms.CharField(label='عنوان', required=True)
    email = forms.EmailField(label='ایمیل', required=True)
    text = forms.CharField(label='متن', min_length=10, max_length=250, widget=forms.Textarea)
