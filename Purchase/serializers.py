from rest_framework import serializers
from Purchase.models import PurchaseOrder,CuttingDetail



class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields = '__all__'



class CuttingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=CuttingDetail
        fields = '__all__'
