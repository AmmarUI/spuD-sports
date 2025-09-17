from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Item

# Create your views here.
def show_main(request):
    context = {
        'user' : 'Ammar',
    }

    return render(request, "main.html", context)   

def show_xml(request):
    item_list = Item.objects.all()
    xml_data = serializers.serialize("xml", item_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    item_list = Item.objects.all()
    json_data = serializers.serialize("json", item_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, item_id):
   item = Item.objects.filter(pk=item_id)
   xml_data = serializers.serialize("xml",item)
   return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, item_id):
   item = Item.objects.filter(pk=item_id)
   json_data = serializers.serialize("json",item)
   return HttpResponse(json_data, content_type="application/json")
