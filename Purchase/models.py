from django.db import models

# Create your models here.
class Supplier(models.Model):
    """docstring for Supplier"""
    
   
       
    SupplierName= models.CharField(max_length=100)
    SupplierType= models.CharField(max_length=30)
    SupplierAddress= models.CharField(max_length=500)
    SupplierContact= models.IntegerField()
    SupplierGST= models.CharField(max_length=15)
    SupplierEMail= models.CharField(max_length=20)
    def __str__(self):
       return '%s,%s' %(self.SupplierName,self.SupplierType)

class PurchaseOrder(models.Model):
    """docstring for PurchaseOrder"""
    def number():
      no=PurchaseOrder.objects.count()

      if no == None :
        return 1
      else:
        return no + 1
    PONO=models.IntegerField(default=number)
    PODate=models.DateTimeField(auto_now=True)
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Amount=models.DecimalField(decimal_places=2,max_digits=10000, default=0)
    def __str__(self):
       return '%s' %(self.supplier)


class PurchaseDetail(models.Model):
     PONO=models.IntegerField()
     RowMatSize=models.CharField(max_length=20)
     RowMatShape=models.CharField(max_length=20)
     RowMatType=models.CharField(max_length=20)
     MaterilQty=models.DecimalField(decimal_places=2,max_digits=10000)
     MaterilUnit=models.CharField(max_length=20)
     MaterilRates=models.DecimalField(decimal_places=2,max_digits=10000)

class PurchaseRawMaterial(models.Model):
    """docstring for PurchaseOrder"""
    def number():
      no=PurchaseRawMaterial.objects.count()
      if no == None :
        return 1
      else:
        return no + 1
    R_No=models.IntegerField(default=number)
    R_Date=models.DateTimeField(auto_now=True)
    R_Invoice=models.IntegerField() 
    R_PONO=models.IntegerField()
    R_Inv_Date=models.DateField()
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    R_Amount=models.DecimalField(decimal_places=2,max_digits=10000)
    def __str__(self):
       return '%s' %(self.supplier)




class RawMaterialDetail(models.Model):
     R2_NO=models.IntegerField()
     R2_Invoice = models.IntegerField()
     R2_RowMatSize=models.CharField(max_length=20)
     R2_RowMatShape=models.CharField(max_length=20)
     R2_RowMatType=models.CharField(max_length=20)
     R2_MaterilQty=models.DecimalField(decimal_places=2,max_digits=10000)
     R2_MaterilUnit=models.CharField(max_length=20)
     R2_MaterilRates=models.DecimalField(decimal_places=2,max_digits=10000)
     R2_Total=models.DecimalField(decimal_places=2,max_digits=10000)

class CuttingDetail(models.Model):     
     R1_RowMatSize=models.CharField(max_length=20)
     R1_RowMatShape=models.CharField(max_length=20)
     R1_RowMatType=models.CharField(max_length=20)
     R1_MaterilQty=models.DecimalField(decimal_places=2,max_digits=10000) 
     R1_MaterilUnit=models.CharField(max_length=20,default='KG')

class Unit(models.Model):     
     Unit_Name=models.CharField(max_length=20,default='KG')
     def __str__(self):
         return '%s' %(self.Unit_Name)

class Type(models.Model):
     Supplier_Type=models.CharField(max_length=20,default='INTERSTATE')
     def __str__(self):
         return '%s' %(self.Supplier_Type)

class Shape(models.Model):
     Row_Mat_Shape=models.CharField(max_length=20,default='pipe')
     def __str__(self):
         return '%s' %(self.Row_Mat_Shape)

class Rawtype(models.Model):
     Row_Mat_Type=models.CharField(max_length=20,default='pipe')
     def __str__(self):
         return '%s' %(self.Row_Mat_Type)


      