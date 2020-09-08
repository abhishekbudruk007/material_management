from rest_framework import serializers
from Purchase.models import PurchaseOrder



class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields = '__all__'


