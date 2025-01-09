from django.urls import path
from . import views

app_name='toyosaka_app'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('Achievements/',views.AchieveView.as_view(),name='Achieve'),
    path('Business_content/',views.ContentView.as_view(),name='Business_content'),
    path('Company_info/',views.info_View.as_view(),name='Company_info'),
    path('Recruitment/',views.Recruitment.as_view(),name='Recruitment'),

]