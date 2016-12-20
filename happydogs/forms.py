from django import forms

DATE_INPUT_FORMATS = ('%d %m %Y')

class ContactForm(forms.Form):
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)