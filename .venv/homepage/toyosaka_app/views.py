from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import Service
from django.views.generic import DetailView
from django.http import HttpResponseRedirect

# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'  # テンプレートで使う変数名


class AchieveView(TemplateView):
    template_name='Achievements.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context

class ContentView(TemplateView):
    template_name='Business_content.html'

class info_View(TemplateView):
    template_name='Company_info.html'

class Recruitment(TemplateView):
    template_name='Recruitment.html'

class ContactView(FormView):
    template_name='contact.html'
    form_class =ContactForm
    success_url=reverse_lazy('toyosaka_app:contact')
    def form_valid(self, form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        subject= 'お問い合わせ:{}'.format(title)

        message = '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:\n{3}'.format(name,email,title,message)
        from_email = 'example@stu.o-hara.ac.jp'
        to_list =['example@stu.o-hara.ac.jp']

        message =EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list)
        # message.send()
        messages.success(self.request,'お問い合わせは正常に送信されまたことにしました')
        # return super().form_valid(form)
        return HttpResponseRedirect(self.success_url)