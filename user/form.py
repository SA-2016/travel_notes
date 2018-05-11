from django import forms

from .models import User

import re


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_email(self):

        '验证邮箱是否合法'

        email = self.cleaned_data['email']
        re_email = '.*@.com'
        p = re.compile( re_email )
        if p.match( email ):
            return True
        else:
            return forms.ValidationError( '非法邮箱', code = 'email_invalid')


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','age','email', 'password','register']

    def clean_email(self):

        '验证邮箱是否合法'

        email = self.cleaned_data['email']
        re_email = '.*@.com'
        p = re.compile( re_email )
        if p.match( email ):
            return True
        else:
            return forms.ValidationError( '非法邮箱', code = 'email_invalid')


