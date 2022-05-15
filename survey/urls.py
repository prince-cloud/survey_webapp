from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = "survey"

urlpatterns = [
    path('', index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('create-survey/', create_survey, name='create_survey'),
    path('edit/<slug:slug>/', edit_survey, name='edit_survey'),
    path('my-surveys/', my_surveys, name='my_surveys'),
    path('<slug:slug>/respond/', survey_response, name='survey_response'),
    path('<slug:slug>/respnoses/', survey_detail, name='survey_detail'),
]