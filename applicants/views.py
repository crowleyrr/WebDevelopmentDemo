from django.shortcuts import render
from django.views.generic import TemplateView

class homePage(TemplateView):
    template_name='home.html'

class volunteerListPage(TemplateView):
    template_name='volunteerlist.html'