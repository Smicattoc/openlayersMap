from django.shortcuts import render
from . import views
from django.template import loader
from django.http import HttpResponse
from map.models import PointFeature
import json


def map(request):
    #template = loader.get_template('maps/index.html')
    #context = {}
    #return HttpResponse(template.render(context, request))
    return render(request, 'maps/index.html')

def create_point(request):
    json_data = json.loads(request.body)
    latitude = json_data["lat"]
    longitude = json_data["long"]
    PointFeature.objects.create(latitude=latitude, longitude=longitude)
    return HttpResponse(status=200)



