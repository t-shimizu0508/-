from django.urls import path
from . import views

app_name='toyosaka_app'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
]