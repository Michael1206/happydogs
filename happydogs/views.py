from django.views.generic.edit import FormView
from forms import  ContactForm
from models import PeriodModel, DogModel
from datetime import date, timedelta as td

class ContactView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/dogs/'

    def form_valid(self, form):
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        delta = end_date - start_date

        for i in range(delta.days + 1):
            date = PeriodModel(date=start_date + td(days=i))
            try:
                date.save()
            except:
                continue

        return super(ContactView, self).form_valid(form)

