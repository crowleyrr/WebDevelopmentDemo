from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ApplicantForm

class homePage(TemplateView):
    template_name='home.html'

class volunteerListPage(TemplateView):
    template_name='volunteerlist.html'

class applicantSignUpPage():
    form = ApplicantForm()

    context = {
        'form': form,
    }

    render('signup.html', context)

