from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, FormView, RedirectView

from core.utils import TODAY, translate_winddir, update_query_quota, create_new_query
from .forms import AuthForm, ForecastDetails
from .models import VisualCrossingAuth, Query

from api.forecast_call import forecast_api_call


class IndexView(RedirectView):
    def get_redirect_url(self):
        url = "about"
        if VisualCrossingAuth.objects.count()>0:
            url = "forecast"

        return url


class AuthView(CreateView):
    model = VisualCrossingAuth
    form_class = AuthForm
    template_name = "authorization.html"

    def get_success_url(self):
        return reverse('forecast')
    
    def get_context_data(self, **kwargs):
        context = super(AuthView, self).get_context_data(**kwargs)
        message = self.request.GET.get("message")
        if message:
            context["message"] = "The provided Visual Crossing Key was invalid. Please provide a valid Visual Crossing Key"
        return context
            
    def form_valid(self, form):
        if VisualCrossingAuth.objects.count()>0:
            for key in VisualCrossingAuth.objects.all():
                if key.vc_key == form.cleaned_data["vc_key"]:
                    key.delete()

            last_query = Query.objects.latest("id")
            last_query.delete()
            create_new_query(0)
        
        return super().form_valid(form)


class ForecastView(FormView):
    form_class = ForecastDetails
    template_name = "forecast.html"

    def get_success_url(self):
        return self.request.path
    
    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        municipality = kwargs.get('municipality', "")
        date = kwargs.get('date', TODAY)
        if municipality is not "":
            raw_forecast = forecast_api_call(municipality)
            if "message" in raw_forecast:
                if raw_forecast["message"].startswith("The Visual"):
                    url = reverse("authorization") + "?message=wrong-key"
                    return redirect(url)
                else:
                    context["message"] = raw_forecast["message"]
            else:
                todays_forecast = {}
                try:
                    for day in raw_forecast["days"]:
                        if day["datetime"] == date:
                            todays_forecast = day
                            break
                    context["temperatureMin"] = f'{todays_forecast["tempmin"]} °C'
                    context["temperatureMax"] = f'{todays_forecast["tempmax"]} °C'
                    context["precipitation"] = f'{todays_forecast["precip"]} mm'
                    context["windSpeed"] = f'{todays_forecast["windspeed"]} km/h'
                    context["windDirection"] = translate_winddir(todays_forecast["winddir"])
                    context["cloudCover"] = f'{todays_forecast["cloudcover"]} %'

                    query_cost = raw_forecast["queryCost"]
                    update_query_quota(query_cost)

                except Exception as e:
                    print("the error is now", e)
            
        return self.render_to_response(context)
    
    def form_valid(self, form):
        municipality = form.cleaned_data["muncipality"]
        date = form.cleaned_data["date"]
        return self.get(self.request, municipality=municipality, date=date)


class QueryView(TemplateView):
    template_name = "query.html"

    def get_context_data(self, **kwargs):
        context = super(QueryView, self).get_context_data(**kwargs)
        if Query.objects.count()>0:
            last_query = Query.objects.latest("id")
            if last_query.day != TODAY:
                last_query.delete()
                create_new_query(0)
                last_query = Query.objects.latest("id")
            context["queryCount"] = last_query.query_count
        
        return context


class AboutView(TemplateView):
    template_name = "about.html"