from django import forms
import re
from django.core.exceptions import ValidationError



class ContactForm(forms.Form):
    name=forms.CharField(label='お名前')
    email=forms.EmailField(label='メールアドレス')
    title=forms.CharField(label='件名')
    message=forms.CharField(label='本文',widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['name'].widget.attrs['placeholder']='お名前を入力してください'
        self.fields['name'].widget.attrs['class'] ='form-control'
        self.fields['email'].widget.attrs['placeholder']='メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class']='form-control'
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