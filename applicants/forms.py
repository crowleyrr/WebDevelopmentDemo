from django import forms
from django.core.exceptions import ValidationError

MONDAY = 'MON'
TUESDAY = 'TUE'
WEDNESDAY = 'WED'
THURSDAY = 'THU'
FRIDAY = 'FRI'
SATURDAY = 'SAT'
SUNDAY = 'SUN'

DAYS_OF_WEEK_CHOICES = [
    (MONDAY, 'Monday'),
    (TUESDAY, 'Tuesday'),
    (WEDNESDAY, 'Wednesday'),
    (THURSDAY, 'Thursday'),
    (FRIDAY, 'Friday'),
    (SATURDAY, 'Saturday'),
    (SUNDAY, 'Sunday'),
]

class ApplicantForm(forms.Form):


    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    age = forms.IntegerField(required=True)
    days_available = forms.MultipleChoiceField(required=True, choices=DAYS_OF_WEEK_CHOICES, label='Days Available to Volunteer')

    def clean_data(self):
        data = self.cleaned_data['first_name', 'last_name', 'age', 'days_available']

        # check if age entered valid:
        if age < 15:
            raise ValidationError(_('Error - age below minimum requirement.  Please apply again later.'))

        return data