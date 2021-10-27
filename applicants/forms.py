from django.forms import ModelForm
from django.db import models
from applicants.models import Volunteer
from django.core.exceptions import ValidationError

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = "__all__"
    def clean_data(self):
        data = self.cleaned_data['first_name', 'last_name', 'age', 'avail_mon', 'avail_tues', 'avail_wed', 'avail_thurs', 'avail_fri']

        # check if age entered valid:
        if self.age < 15:
            raise ValidationError(('Error - age below minimum requirement.  Please apply again later.'))

        return data