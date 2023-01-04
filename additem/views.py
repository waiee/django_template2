from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import Item

# Create your views here.

@login_required
def additemform(request):
    context = {
        'title': 'Add Item Form',
        'year': datetime.now().year,
    }
    context['user'] = request.user

    return render(request,'additem/additemform.html',context)

def additemconfirmation(request):

    newitem_id = request.POST['item_id']
    # newvendor_id = request.POST['vendor_id']
    newitem_name= request.POST['item_name']
    newitem_description = request.POST['item_description']
    newitem_quantity = request.POST['item_quantity']
    newitem_price = request.POST['item_price']


    newitem = Item(item_id = newitem_id,item_name = newitem_name, item_description =newitem_description, item_quantity = newitem_quantity, item_price = newitem_price)
    newitem.save()

    context = {

        'item_id': newitem_id,
        'item_name': newitem_name,
        'item_description': newitem_description,
        # 'vendor_id': newvendor_id,
        'item_quantity': newitem_quantity,
        'item_price': newitem_price,
    }
    return render(request,'additem/additemconfirmation.html',context)