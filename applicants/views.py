from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ApplicantForm

class homePage(TemplateView):
    template_name='home.html'

class volunteerListPage(TemplateView):
    template_name='volunteerlist.html'

class thanksPage(TemplateView):
    template_name='thanks.html'

def applicantSignUpPage(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        print("POST")
        if form.is_valid():
            print("VALID")
            thanksPage()
    else:
        form = ApplicantForm()

    return render(request, 'signup.html', {'form': form})
