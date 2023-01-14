from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render, redirect
from app.models import Item, PurchaseOrder
from django.http import HttpRequest
from django.template import loader

@login_required
def searchItem(request):
    if request.method == "POST":
        searched = request.POST['searched']
        po_id = PurchaseOrder.objects.filter(po_id__contains=searched)
        return render(
            request,
            'viewitem/searchItem.html',
            {
                'searched': searched,
                'po_id' : po_id,
            }
        )
    else:
        return render(request, 
        'viewitem/searchItem.html',{})

def selectItem(request):
    if request.method == "POST":
        selected = request.POST['selected']
        po_id = PurchaseOrder.objects.filter(po_id__contains=selected)
        return render(
            request,
            'viewitem/searchItem.html',
            {
                'selected': selected,
                'po_id' : po_id,
            }
        )
    else:
        return render(request, 
        'viewitem/searchItem.html',{})


def viewItem(request):
    po_list = PurchaseOrder.objects.all()
    return render(
        request,
        'viewitem/viewItem.html',
        {
            'title':'View Purchase Order',
            'year':datetime.now().year,
            'po_list' : po_list,
        }
    )

def backtoHome(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'additem/menu.html',
            {
                'title':'View Item',
                'year': datetime.now().year,
            }
        )