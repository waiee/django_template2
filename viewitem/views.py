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
        # searched = request.POST['searched']
        selected = request.POST['']
        po_id = PurchaseOrder.objects.get(po_id__contains=selected)
        return render(
            request,
            'viewitem/searchItem.html',
            {
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