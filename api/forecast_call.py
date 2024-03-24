import requests
from forecast.models import VisualCrossingAuth

def forecast_api_call(municipality):
    vc_key = ""
    final_response = {"message": "There is no valid Visual Crossing key in the system. Please refer to About section"}

    if VisualCrossingAuth.objects.count()>0:
        vc_key = VisualCrossingAuth.objects.latest("id")
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{municipality}?unitGroup=metric&key={vc_key.vc_key}&contentType=json"
        response = requests.get(url)

        if response.status_code == 200:
            print("the response was OK")
            final_response = response.json()
        elif response.status_code == 400:
            final_response = {"message": "Something's wrong. Check muncipality spelling, please"}
        elif response.status_code == 401:
            vc_key.delete()
            final_response = {"message": "The Visual Crossing key you provided was invalid"}
        else:
            final_response = {"message": "There was an unidentified error. Contact the developer"}
    
    return final_response