from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import VolunteerForm
from .models import Volunteer

class homePage(TemplateView):
    template_name='home.html'

def volunteerListPage(request):
    volunteers = Volunteer.objects.all()
    
    return render(request, template_name='volunteerlist.html', context={'volunteers':volunteers}) 

class thanksPage(TemplateView):
    template_name='thanks.html'
    


def applicantSignUpPage(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        print("POST")
        if form.is_valid():
            print("VALID")
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = VolunteerForm()

    return render(request, 'signup.html', {'form': form})
