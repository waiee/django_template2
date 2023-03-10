"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    staffID = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=5, null=True)

    def __str__(self):
        return str(self.staff_id)

class Vendor(models.Model):
    vendorID = models.CharField(primary_key=True, max_length=10)
    vendorName = models.CharField(max_length=20, null=True)
    vendorAddress = models.CharField(max_length=100, null=True)
    vendorContact = models.BigIntegerField(null=True)

    def __str__(self):
        return str(self.vendor_id)

class QuotationItem(models.Model):
    itemID = models.CharField(primary_key=True, max_length=10)
    vendorID = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE,null=True)
    itemName = models.CharField(max_length=40, null=True)
    quantity = models.PositiveIntegerField(default=None, null=True)
    itemPriceperUnit = models.DecimalField(default=None, null=True, max_digits=8, decimal_places=2)
    qtyNeeded = models.PositiveIntegerField(default=None, null=True)
    
    def __str__(self):
        return str(self.item_id)

class PurchaseOrderProduct(models.Model):
    productID = models.CharField(primary_key=True, max_length=10)
    vendorID = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE)
    productName = models.CharField(max_length=40, null=True)
    quantity = models.PositiveIntegerField(null=True)
    productPriceperUnit = models.DecimalField(default=None, null=True, max_digits=8, decimal_places=2)
    qtyProvided = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.product_id)

class Quotation(models.Model):
    quotationID = models.CharField(primary_key=True, max_length=10)
    staffID = models.ForeignKey(Staff,default=None, on_delete=models.CASCADE)
    itemID = models.ForeignKey(QuotationItem,default=None, on_delete=models.CASCADE)
    vendorID = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE)
    totalPrice = models.DecimalField(default=None, null=True, max_digits=8, decimal_places=2)
    validityDate = models.DateField()
    qtyProvided = models.PositiveIntegerField(null=True)
    quotationStatus = models.CharField(max_length=20)

    def __str__(self):
        return str(self.quotation_id)

class PurchaseOrder(models.Model):
    purchaseOrderID = models.CharField(primary_key=True, max_length=10)
    staffID = models.ForeignKey(Staff,default=None, on_delete=models.CASCADE)
    productID = models.ForeignKey(PurchaseOrderProduct,default=None, on_delete=models.CASCADE)
    quotationID = models.ForeignKey(Quotation,default=None, on_delete=models.CASCADE)
    vendorID = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE)
    qtyNeeded = models.PositiveIntegerField()
    qtyProvided = models.PositiveIntegerField()
    totalPrice = models.DecimalField(default=None, null=True, max_digits=8, decimal_places=2)
    poStatus = models.CharField(max_length=20)

    def __str__(self):
        return str(self.po_id)