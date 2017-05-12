from django import forms

from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('title', 'first_name', 'middle_name', 'last_name', 'known_as', 'dob', 'sex')

        widgets = {
            'dob': forms.DateInput(attrs={'class':'datepicker'}),}