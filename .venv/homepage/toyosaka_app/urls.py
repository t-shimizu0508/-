from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name='toyosaka_app'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('Achievements/',views.AchieveView.as_view(),name='achievements'),
    path('Business_content/',views.ContentView.as_view(),name='Business_content'),
    path('Company_info/',views.info_View.as_view(),name='info'),
    path('Recruitment/',views.Recruitment.as_view(),name='Recruitment'),
    path('service/<int:pk>/',views.ServiceDetailView.as_view(),name='service_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)