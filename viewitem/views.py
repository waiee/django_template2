from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render
from app.models import Item
from django.http import HttpResponse
from django.template import loader

@login_required
def searchItem(request):
    if request.method == "POST":
        searched = request.POST['searched']
        item_id = Item.objects.filter(item_id__contains=searched)
        return render(
            request,
            'viewitem/searchItem.html',
            {
                'searched': searched,
                'item_id' : item_id,
            }
        )
    else:
        return render(request, 
        'viewitem/searchItem.html',{})

def viewItem(request):
    item_list = Item.objects.all()
    return render(
        request,
        'viewitem/viewItem.html',
        {
            'title':'View Item',
            'year':datetime.now().year,
            'item_list' : item_list,
        }
    )