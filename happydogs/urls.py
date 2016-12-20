from django.conf.urls import url, include
import happydogs
from views import ContactView

urlpatterns = [
    url(r'^', ContactView.as_view())
]