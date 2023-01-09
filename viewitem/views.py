from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render
from app.models import Item
from django.http import HttpResponse
from django.template import loader

@login_required
def choose_item(request):

    # Get a list of all the items in the database
    item = Item.objects.all().values()

    context = {
    'year': datetime.now().year,
    'data': item,
    }
    context['user'] = request.user
    
    if request.method == "POST":
        item = Item.objects.all().values()
        item_selected = Item.objects.get(pk=item.id)
        return render(request, 'viewitem/choose_item.html', context)

    return render(request, 'viewitem/choose_item.html', context)
    

def view_item(request):
    # Get the item with the specified id

    item = Item.objects.all().values()
    context = {
    'year': datetime.now().year,
    'data': item,
    }
    context['user'] = request.user

    # return HttpResponse(template.render(context, request))
    return render(request, 'viewitem/view_item.html', context)