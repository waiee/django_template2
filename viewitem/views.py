from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render, redirect
from app.models import Item
from django.http import HttpRequest
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

def backtoHome(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/viewItem'))
    else:
        return render(
            request,
            'additem/viewItem.html',
            {
                'title':'View Item',
                'year': datetime.now().year,
            }
        )