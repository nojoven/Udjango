"""These are the views of the food app"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms
# from django.template import loader

# Create your views here.
def index(request):
    item_list = models.Item.objects.all()
    context = {
        "item_list": item_list,
    }
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse("<h1>This is an item views</h1>")

def detail(request, item_id):
    item = models.Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    form = forms.ItemForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form': form})


def update_item(request, id):
    item = models.Item.objects.get(id=id)
    form = forms.ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form':form, 'item': 'item'})    


def delete_item(request, id):
    item = models.Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item': item})
