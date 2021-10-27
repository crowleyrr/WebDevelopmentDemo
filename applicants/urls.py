from django.urls import path
from .views import homePage, volunteerListPage, applicantSignUpPage, thanksPage
from django.http import HttpResponseRedirect
from django.shortcuts import render


urlpatterns = [
    path('', homePage.as_view(), name='home'),
    path('volunteers', volunteerListPage, name='volunteers'),
    path('signup', applicantSignUpPage, name='signup'),
    path('thanks/', thanksPage.as_view(), name='thanks')
]