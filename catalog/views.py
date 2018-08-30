from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Service, Area, Item


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#List Catalog
def service_list(request):
    service_list = Service.objects.all()
    template = loader.get_template('service/list.html')
    context = {
        'service_list': service_list,
    }
    return HttpResponse(template.render(context, request))


def area_list(request):
    area_list = Area.objects.all()
    template = loader.get_template('area/list.html')
    context = {
        'area_list': area_list,
    }
    return HttpResponse(template.render(context, request))

def item_list(request):
    item_list = Item.objects.all()
    template = loader.get_template('item/list.html')
    context = {
        'item_list': item_list,
    }
    return HttpResponse(template.render(context, request))

#Detal Catalog
def service_detail(request, service_id):
    try:
        service = Service.objects.get(pk=service_id)
    except Service.DoesNotExist:
        raise Http404("Service does not exist")
    return render(request, 'service/detail.html', {'service': service})


def area_detail(request, area_id):
    try:
        area = Area.objects.get(pk=area_id)
    except Area.DoesNotExist:
        raise Http404("Area does not exist")
    return render(request, 'area/detail.html', {'area': area})

def item_detail(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'item/detail.html', {'item': item})

#CRUD Catalog
