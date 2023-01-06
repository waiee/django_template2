from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Item

def choose_item(request):
    # Get a list of all the items in the database
    items = Item.objects.all()
    return render(request, 'viewitem/choose_item.html', {'items': items})

def view_item(request, item_id):
    # Get the item with the specified id
    item = Item.objects.get(id=item_id)
    return render(request, 'viewitem/view_item.html', {'item': item})