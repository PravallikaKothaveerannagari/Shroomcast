from django.urls import path
from forecast.views import AuthView, ForecastView, AboutView, IndexView, QueryView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('authorization', AuthView.as_view(), name="authorization" ),
    path('authorization/<str:message>', AuthView.as_view(), name="authorization_with_msg" ),
    path('forecast', ForecastView.as_view(), name="forecast"),
    path('query', QueryView.as_view(), name="query"),
    path('about', AboutView.as_view(), name="about")
]