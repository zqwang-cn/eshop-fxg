#encoding:utf-8
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import re

class SigninForm(forms.Form):
    phone_number=forms.CharField(label=u'手机号',min_length=11,max_length=11,required=True)
    password = forms.CharField(label=u'密码', min_length=5,widget=forms.PasswordInput())
    next=forms.CharField(widget=forms.HiddenInput(),required=False)

    def clean_phone_number(self):
        phone_number=self.cleaned_data['phone_number']
        if re.match(r'^1\d{10}$',phone_number):
            return phone_number
        else:
            raise forms.ValidationError('手机号格式不正确。')

    def clean(self):
        super(SigninForm,self).clean()
        if len(self.errors)!=0:
            print self.errors
            return
        username=self.cleaned_data['phone_number']
        password=self.cleaned_data['password']
        user=authenticate(username=username,password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码错误。')

class SignupForm(forms.Form):
    phone_number=forms.CharField(label=u'手机号',min_length=11,max_length=11,required=True)
    password = forms.CharField(label=u'密码', min_length=5,widget=forms.PasswordInput())
    confirm = forms.CharField(label=u'确认密码', min_length=5,widget=forms.PasswordInput())

    def clean_phone_number(self):
        phone_number=self.cleaned_data['phone_number']
        if re.match(r'^1\d{10}$',phone_number):
            return phone_number
        else:
            raise forms.ValidationError('手机格式不正确。')

    def clean_confirm(self):
        password=self.cleaned_data['password']
        confirm=self.cleaned_data['confirm']
        if password!=confirm:
            raise forms.ValidationError('密码不一致。')
        return confirm

    def clean(self):
        super(SignupForm,self).clean()
        if len(self.errors)!=0:
            return
        phone_number=self.cleaned_data['phone_number']
        try:
            User.objects.get(username=phone_number)
        except:
            return
        raise forms.ValidationError('此手机号已经注册。')

