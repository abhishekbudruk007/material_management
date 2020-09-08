from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone
from django import forms

from .models import Supplier
from .models import PurchaseOrder
from .models import PurchaseRawMaterial
from .models import Unit
from .models import Type
from .models import Shape
from .models import Rawtype




class Add_Supplier(forms.Form):
    """docstring for Supplier"""

    Supplier_Name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Supplier Name', "maxlength": "20",
               'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '}))
    Supplier_Type = forms.ModelChoiceField(queryset=Type.objects.all(), label='SupplierType',
                                           widget=forms.Select(attrs={'class': 'form-control'}))
    Supplier_Address = forms.CharField(label='SupplierAddress', max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Suppliers Address'}))
    Supplier_Contact = forms.CharField(label='SupplierContact', min_length=10, widget=forms.TextInput(
        attrs={'type': 'tel', 'minlength': '10', 'class': 'form-control', 'placeholder': 'Enter Mobile Number',
               'maxlength': 10, 'pattern': '[\d{10}]+', 'title': 'Enter digits Only '}))
    Supplier_GST = forms.CharField(label='SupplierGST', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter GST Number'}))
    Supplier_EMail = forms.EmailField(label='SupplierEMail', max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}))

    class Meta:
        model = Supplier
        fields = ['SupplierName', 'SupplierType', 'SupplierAddress', 'SupplierContact', 'SupplierGST', 'SupplierEMail']


def number():
      no=PurchaseOrder.objects.count()

      if no == None :
        return 1
      else:
        return no + 1


class Purchase_Order(forms.Form):
    """docstring for PurchaseOrder"""
    PO_NO=forms.IntegerField(label='PO No',initial=number,widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    Supplier=forms.ModelChoiceField(queryset=Supplier.objects.all(),label='Suppiler Name',
                                           widget=forms.Select(attrs={'class': 'form-control'}))
    Row_Mat_Size=forms.DecimalField(label='RawMatSize',min_value=0,decimal_places=2,max_digits=10000,widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    Row_Mat_Shape=forms.ModelChoiceField(queryset=Shape.objects.all(),label='RawMatShape', widget=forms.Select(attrs={'class': 'form-control'}))
    Row_Mat_Type=forms.ModelChoiceField(queryset=Rawtype.objects.all(),label='RawMatType', widget=forms.Select(attrs={'class': 'form-control'}))
    Materil_Qty=forms.DecimalField(label='MaterialQty',decimal_places=0,min_value=0,max_digits=10000,widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter QTY'}))
    Materil_Unit=forms.ModelChoiceField(queryset=Unit.objects.all(),label='MaterialUnit',widget=forms.Select(attrs={'class': 'form-control'}))
    Materil_Rate=forms.DecimalField(label='MaterialRate',min_value=0,max_digits=10000,widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = PurchaseOrder
        fields = ['PO_NO', 'Supplier', 'Row_Mat_Size', 'Row_Mat_Shape', 'Row_Mat_Type', 'Materil_Qty','Materil_Unit','Materil_Rate']


def number1():
      no=PurchaseRawMaterial.objects.count()

      if no == None :
        return 1
      else:
        return no + 1


class Purchase_Entry(forms.Form):
    R1_PO_NO=forms.IntegerField(label='PO_No',widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    Supplier=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'}))
    # amount=forms.DecimalField(label='Total',max_digits=10000,initial=0,widget=forms.TextInput(
    #     attrs={'class': 'form-control'}))
    inv_NO=forms.IntegerField(label='Inv_No',min_value=0,widget=forms.TextInput(
        attrs={'class': 'form-control','readonly':'readonly'}))
    inv_Date=forms.DateField( required=False, widget =forms.SelectDateWidget(),label='InvDate',initial=timezone.now(),)
    R1_Row_Mat_Size=forms.DecimalField(label='RawMatSize',min_value=0,decimal_places=2,max_digits=10000,widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    R1_Row_Mat_Shape=forms.ModelChoiceField(queryset=Shape.objects.all(),label='RawMatShape',widget=forms.Select(attrs={'class': 'form-control'}))
    R1_Row_Mat_Type=forms.ModelChoiceField(queryset=Rawtype.objects.all(),label='RawMatType',widget=forms.Select(attrs={'class': 'form-control'}))
    R1_Materil_Qty=forms.DecimalField(label='MaterialQty',min_value=0,decimal_places=0,max_value=10000,widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    R1_Materil_Unit=forms.ModelChoiceField(queryset=Unit.objects.all(),label='MaterialUnit',widget=forms.Select(attrs={'class': 'form-control'}))
    R1_Materil_Rate=forms.DecimalField(label='MaterialRate',min_value=0,max_value=10000,widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = PurchaseRawMaterial
        fields = ['R1_PO_NO', 'Supplier', 'amount', 'inv_NO', 'inv_Date', 'R1_Row_Mat_Size','R1_Row_Mat_Shape','R1_Row_Mat_Type','R1_Materil_Qty','R1_Materil_Unit','R1_Materil_Rate']


class sendcutting (forms.Form): 
    id_cut=forms.IntegerField(label='ID',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    R4_Row_Mat_Size=forms.CharField(label='RawMatSize',max_length=20,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    R4_Row_Mat_Shape=forms.CharField(label='RawMatShape',max_length=20,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    R4_Row_Mat_Type=forms.CharField(label='RawMatType',max_length=20,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    R4_Row_Mat_Unit=forms.CharField(label='Unit',max_length=20,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    R4_Materil_Qty=forms.DecimalField(label='MaterialQty',decimal_places=2,max_digits=10000,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    R4_Materil_cut=forms.DecimalField(label='Cutting_Material',decimal_places=2,max_digits=10000)
    


    
    