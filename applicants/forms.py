from django import forms
from django.core.exceptions import ValidationError

class ApplicantForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    age = forms.IntegerField(required=True)
    avail_mon = forms.BooleanField(required=True)
    avail_tues = forms.BooleanField(required=True)
    avail_wed = forms.BooleanField()
    avail_thurs = forms.BooleanField()
    avail_fri = forms.BooleanField()

    def clean_data(self):
        data = self.cleaned_data['first_name', 'last_name', 'age', 'avail_mon', 'avail_tues', 'avail_wed', 'avail_thurs', 'avail_fri']

        # check if age entered valid:
        if age < 15:
            raise ValidationError(_('Error - age below minimum requirement.  Please apply again later.'))

        return data