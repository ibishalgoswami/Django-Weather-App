from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from datetime import datetime
import numpy as np
from .models import Weather_details
from django.http import HttpResponse, Http404

# Create your views here.

class WeatherView(TemplateView):    
    template_name = "index.html"
    
    def post(self, request):
        try:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=924a96f7106bc1c738959ef67935d05f'
            city=request.POST['searchfield']
            r = requests.get(url.format(city)).json()
            f_temperature=r["main"]["temp"]
            celsius_temp = (f_temperature - 32) * 5/9
            celsius_temp=round(celsius_temp, 2)
            city_weather = {
                'date':datetime.now().strftime("%A"),
                'time':datetime.now().strftime("%I:%M %p"),
                'city': r["name"],
                'country':r['sys']['country'],
                'temperature':celsius_temp,
                'description': r["weather"][0]["description"],
                'icon': r["weather"][0]["icon"],
                'temp_min': r["main"]["temp_min"],
                'temp_max': r["main"]["temp_max"],
                }
            Weather_details.objects.create(city = city, temp = celsius_temp, weather_details = r["weather"][0]["description"])
            context = city_weather
            return self.render_to_response(context)
        except KeyError as name:
            return self.render_to_response({'error':'City not found'})

    def get(self, request):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=924a96f7106bc1c738959ef67935d05f'
        city="kolkata"
        r = requests.get(url.format(city)).json()
        f_temperature=r["main"]["temp"]
        celsius_temp = (f_temperature - 32) * 5/9
        celsius_temp=round(celsius_temp, 2)
        city_weather = {
            'date':datetime.now().strftime("%A"),
            'time':datetime.now().strftime("%I:%M %p"),
            'city': r["name"],
            'country':r['sys']['country'],
            'temperature':celsius_temp,
            'description': r["weather"][0]["description"],
            'icon': r["weather"][0]["icon"],
            'temp_min': r["main"]["temp_min"],
            'temp_max': r["main"]["temp_max"],
                }
        # Weather_details.objects.create(city = city, temp = celsius_temp, weather_details = r["weather"][0]["description"])
        context = city_weather
        return self.render_to_response(context)    
        
            

   
   
    
