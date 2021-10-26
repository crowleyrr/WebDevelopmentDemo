from django.urls import path
from .views import homePage, volunteerListPage

urlpatterns = [
    path('', homePage.as_view(), name='home'),
    path('/volunteers', volunteerListPage.as_view(), name='volunteers')
]