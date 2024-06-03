from django.shortcuts import render
from django.contrib import messages
import requests  
import datetime

# Create your views here.

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'dhaka'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=dbe0a28acd55309d5dc7eabeda308ef1'
    PARAMS = {'units': 'metric'}



    try:
        data = requests.get(url, params=PARAMS).json()

        if 'weather' in data and 'main' in data:
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
            temp = data['main']['temp']
        else:
            raise ValueError("Incomplete data received from API")

        day = datetime.date.today()
        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False
        })
    except Exception as e:
        messages.error(request, 'Entered city data is not available from the API')
        description = 'N/A'
        icon = 'N/A'
        temp = 'N/A'
        day = datetime.date.today()
        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': 'Entered city data is not available from the API',
            'exception_occurred': True
        })