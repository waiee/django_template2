from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render
from app.models import Item

@login_required
def choose_item(request):
    context = {
    'title': 'View Item',
    'year': datetime.now().year,
    }
    context['user'] = request.user

    # Get a list of all the items in the database
    items = Item.objects.all()
    return render(request, 'viewitem/choose_item.html', {'item': items}, context)

def view_item(request):
    # Get the item with the specified id
    context = {

        'item_id': item_id,
        'item_name': item_name,
        'item_description': item_description,
        'vendor_id': vendor,
        'item_quantity': item_quantity,
        'item_price': item_price,
    }
    return render(request, 'viewitem/view_item.html', context)