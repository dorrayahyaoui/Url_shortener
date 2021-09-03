from django.urls import path , re_path
from . import views

app_name = 'testMainApi'
urlpatterns =[
    path('generate_url/',views.Url_serviceViewSet.as_view(),name='generate_url'),
    path('url_staics/<pk>/',views.Url_staticsViewSet.as_view(),name='generate_url'),
]
