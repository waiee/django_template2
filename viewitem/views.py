from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render
from app.models import Item
from django.http import HttpResponse
from django.template import loader

@login_required
def viewItem(request):

    # Get a list of all the items in the database
    item = Item.objects.all().values()
    
    context = {
        'year': datetime.now().year,
        'data': item,
        }
    context['user'] = request.user
    return render(request, 'viewitem/choose_item.html', context)