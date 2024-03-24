import datetime

from forecast.models import Query

TODAY = datetime.date.today()

def generate_date_choices():
    date = TODAY
    choices = []
    for i in range(14):
        choices.append((str(date), str(date)))
        date += datetime.timedelta(days=1)
    return tuple(choices)

def translate_winddir(winddir_value):
    winddir = ""
    if 349 < winddir_value < 361 or 0 <= winddir_value < 19:
        winddir = "N"
    elif 19 < winddir_value < 39:
        winddir = "N/NE"
    elif 39 < winddir_value < 59:
        winddir = "NE"
    elif 59 < winddir_value < 79:
        winddir = "E/NE"
    elif 79 < winddir_value < 109:
        winddir = "E"
    elif 109 < winddir_value < 129:
        winddir = "E/SE"
    elif 129 < winddir_value < 149:
        winddir = "SE"
    elif 149 < winddir_value < 169:
        winddir = "S/SE"
    elif 169 < winddir_value < 199:
        winddir = "S"
    elif 199 < winddir_value < 219:
        winddir = "S/SW"
    elif 219 < winddir_value < 239:
        winddir = "SW"
    elif 239 < winddir_value < 259:
        winddir = "SW"
    elif 259 < winddir_value < 289:
        winddir = "W"
    elif 289 < winddir_value < 309:
        winddir = "W/NW"
    elif 309 < winddir_value < 329:
        winddir = "NW"
    elif 329 < winddir_value < 349:
        winddir = "N/NW"

    return winddir

def update_query_quota(value):

    all_queries = Query.objects.all()
    if all_queries.exists():
        current_object = Query.objects.latest("id")
        if current_object.day != datetime.date.today():
            current_object.delete()
            create_new_query(value)
        else:
            new_value = current_object.query_count + value
            current_object.query_count = new_value
            current_object.save()
    else:
        create_new_query(value)
        

def create_new_query(value):
    new_query_count = Query(query_count = value)
    new_query_count.save()