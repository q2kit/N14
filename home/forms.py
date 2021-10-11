from cProfile import label

import phone as phone
from django.forms import ModelForm
from django import forms
import re
from .models import Customer


class RegisterForm(forms.Form):
    name = forms.CharField(label="Họ và tên:", max_length=40)
    phone = forms.CharField(label="Số điện thoại:", max_length=20)
    password1 = forms.CharField(label="Mật khẩu:", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Nhập lại mật khẩu:", widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        phone = self.cleaned_data['phone']
        if not re.search(r'^\w+&', phone):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            Customer.objects.get(phone=phone)
        except Customer.DoesNotExist:
            return phone
        raise forms.ValidationError("Tài khoản đã tồn tại")


class RegisterForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
