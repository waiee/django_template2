from django.contrib import admin
from app.models import Staff, Vendor, Item, Product, Quotation, PurchaseOrder

admin.site.register(Item)
admin.site.register(Staff)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Quotation)
admin.site.register(PurchaseOrder)
