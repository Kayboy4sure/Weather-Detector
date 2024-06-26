from django.shortcuts import render
import json
import urllib.request


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        if city == '':
            city = ''
            data = {}
        else:
            res = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=2a8c7587979f9cdd04728fb119584ba1').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "weather": str(json_data['weather'][0]['main']),
                "description": str(json_data['weather'][0]['description']),
                "coordinate": str(json_data['coord']['lat']) + ',' +
                              str(json_data['coord']['lon']),
                "temp": str(json_data['main']['temp']) + 'k',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
