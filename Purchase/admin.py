from django.contrib import admin
from .models import Supplier
from .models import PurchaseOrder
from .models import PurchaseDetail
from .models import PurchaseRawMaterial
from .models import RawMaterialDetail
from .models import CuttingDetail
from .models import Unit
from .models import Type
from .models import Shape
from .models import Rawtype

# Register your models here.


class PurchaseDetailadmin(admin.ModelAdmin):

	list_display=['PONO','RowMatSize','RowMatShape','RowMatType','MaterilQty','MaterilUnit','MaterilRates']
	
	class Meta:
		model = PurchaseDetail

class PurchaseOrderadmin(admin.ModelAdmin):

	list_display=['PONO','PODate','supplier','Amount']
	
	class Meta:
		model = PurchaseDetail

class Supplieradmin(admin.ModelAdmin):

	list_display=['SupplierName','SupplierType','SupplierAddress','SupplierContact','SupplierGST','SupplierEMail']
	
	class Meta:
		model = PurchaseDetail

class PurchaseRawMaterialadmin(admin.ModelAdmin):

	list_display=['R_No','R_Date','R_Invoice','R_PONO','R_Inv_Date','supplier','R_Amount']
	
	class Meta:
		model = PurchaseRawMaterial

class RawMaterialDetailadmin(admin.ModelAdmin):

	list_display=['R2_NO','R2_Invoice','R2_RowMatSize','R2_RowMatShape','R2_RowMatType','R2_MaterilQty','R2_MaterilUnit','R2_MaterilRates','R2_Total']
	
	class Meta:
		model = PurchaseDetail

class CuttingDetailadmin(admin.ModelAdmin):

	list_display=['R1_RowMatSize','R1_RowMatShape','R1_RowMatType','R1_MaterilQty']

	class Meta:
		model = CuttingDetail

class Unitadmin(admin.ModelAdmin):

	list_display=['Unit_Name']
	
	class Meta:
		model = Unit

class Typeadmin(admin.ModelAdmin):

	list_display=['Supplier_Type']
	
	class Meta:
		model = Type

class Shapeadmin(admin.ModelAdmin):

	list_display=['Row_Mat_Shape']
	
	class Meta:
		model = Shape	

class Rawtypeadmin(admin.ModelAdmin):

	list_display=['Row_Mat_Type']
	
	class Meta:
		model = Rawtype	


admin.site.register(Supplier,Supplieradmin)
admin.site.register(PurchaseOrder,PurchaseOrderadmin)
admin.site.register(PurchaseDetail,PurchaseDetailadmin)
admin.site.register(PurchaseRawMaterial,PurchaseRawMaterialadmin)
admin.site.register(RawMaterialDetail,RawMaterialDetailadmin)
admin.site.register(CuttingDetail,CuttingDetailadmin)
admin.site.register(Unit,Unitadmin)
admin.site.register(Type,Typeadmin)
admin.site.register(Shape,Shapeadmin)
admin.site.register(Rawtype,Rawtypeadmin)