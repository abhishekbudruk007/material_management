import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
from .models import PurchaseOrder
from django.core import serializers
from Purchase.serializers import PurchaseOrderSerializer

class GetSuppliers(APIView):
    def post(self, request, *args,**kwargs):
        data = json.loads(request.POST.get('data'))
        po_no = data.get('po_no', '')

        print("po_no",po_no)
        suppliers_name = ''
        try:
            suppliers_name = PurchaseOrder.objects.filter(PONO=po_no)[0].supplier.SupplierName
            print("suppliers_name",suppliers_name)
        except Exception as e:
            print("error ", e)
        return Response(suppliers_name)