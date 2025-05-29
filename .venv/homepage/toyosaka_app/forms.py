from django import forms
import re
from django.core.exceptions import ValidationError



class ContactForm(forms.Form):
    name=forms.CharField(label='お名前')
    pronunciation=forms.CharField(label='ふりがな')
    email=forms.EmailField(label='メールアドレス')
    tel=forms.CharField(label='電話番号')
    title=forms.CharField(label='件名')
    message=forms.CharField(label='本文',widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['name'].widget.attrs['placeholder']='お名前を入力してください'
        self.fields['name'].widget.attrs['class'] ='form-control'
        self.fields['pronunciation'].widget.attrs['placeholder']='ふりがなを入力してください'
        self.fields['pronunciation'].widget.attrs['class'] ='form-control'
        self.fields['email'].widget.attrs['placeholder']='メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['tel'].widget.attrs['placeholder']='電話番号を入力してください(ハイフンなし)'
        self.fields['tel'].widget.attrs['class'] ='form-control'
        self.fields['title'].widget.attrs['placeholder']='タイトルを入力してください'
        self.fields['title'].widget.attrs['class']='form-control'
        self.fields['message'].widget.attrs['placeholder']='本文を入力してください'
        self.fields['message'].widget.attrs['class']='form-control'
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if not re.match(email_regex, email):
            raise ValidationError('無効なメールアドレスです。有効な形式で入力してください。')

        return email
    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        tel_regex = r'^(\+81\d{9,10}|0\d{9,10})$'
        if not re.match(tel_regex, tel):
            raise ValidationError('電話番号の形式が正しくありません')
        return tel