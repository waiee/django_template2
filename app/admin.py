from django.contrib import admin
from app.models import Staff, Vendor, QuotationItem, PurchaseOrderProduct, Quotation, PurchaseOrder

admin.site.register(QuotationItem)
admin.site.register(PurchaseOrderProduct)
admin.site.register(Staff)
admin.site.register(Vendor)
admin.site.register(Quotation)
admin.site.register(PurchaseOrder)
