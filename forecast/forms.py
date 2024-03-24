from django import forms

from core.utils import generate_date_choices
from django.core.validators import MinLengthValidator, RegexValidator
from .models import VisualCrossingAuth

class AuthForm(forms.ModelForm):

    vc_key = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'sc-input'
        }),
        validators=[
            MinLengthValidator(25),
            RegexValidator(
                '^(\w+\d+|\d+\w+)+$',
                message="Visual Crossing key must be a combination of characters and numbers"
            )
        ]
    )
    class Meta:
        model = VisualCrossingAuth
        fields = ["vc_key"]

class ForecastDetails(forms.Form):
    muncipality = forms.CharField(max_length=100)
    date = forms.ChoiceField(choices = generate_date_choices())

    muncipality.widget.attrs.update({"class": "sc-input"})
    date.widget.attrs.update({"class": "bg-transparent",
                              "style": "border: none; border-bottom: 1px solid #3b1e00; padding: 3px; color: #3b1e00"})