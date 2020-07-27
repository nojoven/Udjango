"""These are the views of the food app"""
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.template import loader

# Create your views here.
def index(request):
    item_list = models.Item.objects.all()
    context = {
        "item_list": item_list,
    }
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse("<h1>This is an item views</h1>")
