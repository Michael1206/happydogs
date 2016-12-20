from django.views.generic.edit import FormView
from forms import  ContactForm
from models import PeriodModel, DogModel

class ContactView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/dogs/'

    def form_valid(self, form):
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']

        # form.send_email()
        return super(ContactView, self).form_valid(form)

