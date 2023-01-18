from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import QuotationItem, Vendor

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

    newitem_id = request.POST['itemID']
    newvendor_id = request.POST['vendorID']
    newitem_name= request.POST['itemName']
    newitem_quantity = request.POST['quantity']
    newitem_price = request.POST['itemPriceperUnit']
    vendor = Vendor.objects.get(pk=newvendor_id)
    
    newitem = QuotationItem(itemID = newitem_id, vendorID= vendor, itemName = newitem_name, quantity = newitem_quantity, itemPriceperUnit = newitem_price)
    newitem.save()

    context = {

        'itemID': newitem_id,
        'itemName': newitem_name,
        'vendorID': vendor,
        'quantity': newitem_quantity,
        'itemPriceperUnit': newitem_price,
    }
    return render(request,'additem/additemconfirmation.html',context)