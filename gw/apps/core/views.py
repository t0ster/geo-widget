from django.views.generic import FormView
from django import forms
from django import http
from django.utils import simplejson as json
from pygeocoder import Geocoder


class LocationsForm(forms.Form):
    q = forms.CharField(label="Search Location")

    def autocomplete(self):
        results = Geocoder.geocode(self.cleaned_data["q"])
        return [r.formatted_address for r in results]


def locations_autocomplete(request):
    form = LocationsForm(request.REQUEST)
    if form.is_valid():
        return http.HttpResponse(json.dumps(form.autocomplete()),
                                 content_type='application/json'
                                )


class LocationsView(FormView):
    template_name = "index.haml"
    form_class = LocationsForm
