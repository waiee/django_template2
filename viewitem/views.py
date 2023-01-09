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

def view_item(request, item_id):
    # Get the item with the specified id
    item = Item.objects.get(id=item_id)
    return render(request, 'viewitem/view_item.html', {'item': item})