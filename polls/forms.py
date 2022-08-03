from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator
from .models import Course, UserProfileInfo


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


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class ProfileChangeInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        exclude = ('user',)
        labels = {
            'gender': 'جنسیت',
            'biography': 'بیوگرافی'
        }
        widgets = {
            'biography': forms.Textarea()
        }

class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'name': 'نام درس',
            'department': 'دانشکده',
            'course_number': 'شماره درس',
            'group_number': 'شماره گروه',
            'teacher': 'استاد درس',
            'start_time': 'ساعت شروع',
            'end_time': 'ساعت پایان',
            'first_day': 'روز اول',
            'second_day': 'روز دوم'
        }
        widgets = {
            'start_time': forms.TimeInput(format='%H:%M'),
            'end_time': forms.TimeInput(format='%H:%M')
        }
