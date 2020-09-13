from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout

from django.http import HttpResponseRedirect
import decimal
# from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import Add_Supplier
from .form import Purchase_Order
from .form import Purchase_Entry
from .form import sendcutting
from .models import Supplier
from .models import PurchaseDetail
from .models import PurchaseOrder
from .models import RawMaterialDetail
from .models import PurchaseRawMaterial
from .models import CuttingDetail


# Create your views
def Home(request):
    if request.user.is_authenticated:
        TEMPLATES = 'home.html'
        return render(request, TEMPLATES)
    else:
        messages.error(request, 'Please login Again')
        # from = Login()
        return HttpResponseRedirect("/")


def Login(request):
    if request.method == 'POST':

        username = request.POST['Fname']
        password = request.POST['Lword']
        print("Code is here")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print("Code is here")
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('/Home/')

        else:
            messages.error(request, 'Please Provide Correct Username and Password.')
            # from = Login()
            return render(request, 'logindesign.html')

    else:

        return render(request, 'logindesign.html')

from django.contrib.auth import logout
def Logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def Supplier_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Add_Supplier(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            obj = Supplier()  # gets new object
            obj.SupplierName = form.cleaned_data['Supplier_Name']
            obj.SupplierType = form.cleaned_data['Supplier_Type']
            obj.SupplierAddress = form.cleaned_data['Supplier_Address']
            obj.SupplierContact = form.cleaned_data['Supplier_Contact']
            obj.SupplierGST = form.cleaned_data['Supplier_GST']
            obj.SupplierEMail = form.cleaned_data['Supplier_EMail']
            obj.save()
            # print("Data Saved")
            messages.success(request, 'Supplier Added Successfully')
            # messages.success(request,f'Submission successful')
            form = Add_Supplier()
            # messages.success(request, f'Your account has been updated!')
            # return http.HttpResponseRedirect('/Add_Supplier/')
            # return redirect("r'^Home/Add_Supplier/'")
            return render(request, 'Supplier.html', {'form': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Add_Supplier()
        return render(request, 'Supplier.html', {'form': form})


'''def detailed (self, requeste):
     form2= PurchaseDetail.object.all()
     return render(request, 'Purchase_Order.html', {'form2':form3})'''


def ponumber():
    no = PurchaseDetail.objects.count()
    # Newpo= form.cleaned_data['PO_NO']
    if no == None:
        return 1
    else:
        return no


def stockreport():
    sto = CuttingDetail.objects.filter


def Purchase_Material(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Purchase_Order(request.POST)

        form2 = PurchaseDetail.objects.all()
        print()
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            obj = PurchaseOrder()  # gets new object
            obj1 = PurchaseDetail()

            obj.supplier = form.cleaned_data['Supplier']
            obj.save()

            obj1.PONO = PurchaseOrder.objects.order_by('-PONO')[0].PONO
            obj1.RowMatSize = form.cleaned_data['Row_Mat_Size']
            obj1.RowMatShape = form.cleaned_data['Row_Mat_Shape']
            obj1.RowMatType = form.cleaned_data['Row_Mat_Type']
            obj1.MaterilQty = form.cleaned_data['Materil_Qty']
            obj1.MaterilUnit = form.cleaned_data['Materil_Unit']
            obj1.MaterilRates = form.cleaned_data['Materil_Rate']
            obj1.save()
            form1 = PurchaseOrder()
            form4 = PurchaseDetail()
            form5 = form.cleaned_data['PO_NO']
            no = PurchaseOrder.objects.count()
            form2 = PurchaseDetail.objects.filter(PONO=no)
            print("form2", list(form2))
            messages.success(request, 'Puchase Order Generated')


            # if (obj.supplier == form.cleaned_data['Supplier']):

                # obj.supplier = form.cleaned_data['Supplier']
                # obj.save()
                #
                # obj1.PONO = PurchaseOrder.objects.order_by('-PONO')[0].PONO
                # obj1.RowMatSize = form.cleaned_data['Row_Mat_Size']
                # obj1.RowMatShape = form.cleaned_data['Row_Mat_Shape']
                # obj1.RowMatType = form.cleaned_data['Row_Mat_Type']
                # obj1.MaterilQty = form.cleaned_data['Materil_Qty']
                # obj1.MaterilUnit = form.cleaned_data['Materil_Unit']
                # obj1.MaterilRates = form.cleaned_data['Materil_Rate']
                # obj1.save()
                # form1 = PurchaseOrder()
                # form4 = PurchaseDetail()
                # form5 = form.cleaned_data['PO_NO']
                # no = PurchaseOrder.objects.count()
                # form2 = PurchaseDetail.objects.filter(PONO=no)
                # print("form2",list(form2))
                # messages.success(request, 'Puchase Order Generated')


                # print("Here is code 2")
            # else:
            #
            #     obj1.PONO = PurchaseOrder.objects.order_by('-PONO')[0].PONO
            #     obj1.RowMatSize = form.cleaned_data['Row_Mat_Size']
            #     obj1.RowMatShape = form.cleaned_data['Row_Mat_Shape']
            #     obj1.RowMatType = form.cleaned_data['Row_Mat_Type']
            #     obj1.MaterilQty = form.cleaned_data['Materil_Qty']
            #     obj1.MaterilUnit = form.cleaned_data['Materil_Unit']
            #     obj1.MaterilRates = form.cleaned_data['Materil_Rate']
            #     obj1.save()
            #
            #     form1 = PurchaseOrder()
            #     form4 = PurchaseDetail()
            #     form5 = form.cleaned_data['PO_NO']
            #     no = PurchaseOrder.objects.count()
            #     form2 = PurchaseDetail.objects.filter(PONO=no)

                # print("Here is code 1")
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
        # if a GET (or any other method) we'll create a blank form
        else:
            print(form.errors)
    else:

        form = Purchase_Order()
        form5 = 0

        number = PurchaseOrder.objects.count()
        number = number + 1
        # print(number)
        form2 = PurchaseDetail.objects.filter(PONO=number)

    return render(request, 'Purchase_Order.html', {'form': form, 'form2': form2, 'form5': form5})


def cleartext():
    pass
    return True


def add_purchase(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Purchase_Entry(request.POST)

        # form2=Purchase_EntryDetail(request.POST)
        # check whether it's valid:
        import pdb;
        pdb.set_trace()
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            print("Code is here0")
            obj = PurchaseRawMaterial()  # gets new object
            obj1 = RawMaterialDetail()
            obj2 = CuttingDetail()
            if (obj.R_Invoice == form.cleaned_data['inv_NO']):
                obj.R_Invoice = form.cleaned_data['inv_NO']
                obj.R_PONO = form.cleaned_data['R1_PO_NO']
                obj.R_Inv_Date = form.cleaned_data['inv_Date']
                obj.supplier = form.cleaned_data['Supplier']
                obj.save()
                obj1.R2_RowMatSize = form.cleaned_data['R1_Row_Mat_Size']
                obj1.R2_RowMatShape = form.cleaned_data['R1_Row_Mat_Shape']
                obj1.R2_RowMatType = form.cleaned_data['R1_Row_Mat_Type']
                obj1.R2_MaterilQty = form.cleaned_data['R1_Materil_Qty']
                obj1.R2_MaterilUnit = form.cleaned_data['R1_Materil_Unit']
                obj1.R2_MaterilRates = form.cleaned_data['R1_Materil_Rate']
                obj1.R2_Total = obj1.R2_MaterilRates * obj1.R2_MaterilQty
                obj.R_Amount = + obj1.R2_Total

                if CuttingDetail.objects.filter(R1_RowMatSize=form.cleaned_data['R1_Row_Mat_Size']).filter(
                        R1_RowMatShape=form.cleaned_data['R1_Row_Mat_Shape']).filter(
                        R1_RowMatType=form.cleaned_data['R1_Row_Mat_Type']).filter(
                        R1_MaterilUnit=form.cleaned_data['R1_Materil_Unit']):

                    sto = CuttingDetail.objects.filter(R1_RowMatSize=form.cleaned_data['R1_Row_Mat_Size']).filter(
                        R1_RowMatShape=form.cleaned_data['R1_Row_Mat_Shape']).filter(
                        R1_RowMatType=form.cleaned_data['R1_Row_Mat_Type']).filter(
                        R1_MaterilUnit=form.cleaned_data['R1_Materil_Unit']).first().R1_MaterilQty

                    sto = sto + form.cleaned_data['R1_Materil_Qty']
                    print(sto)
                    CuttingDetail.objects.filter(R1_RowMatSize=form.cleaned_data['R1_Row_Mat_Size']).filter(
                        R1_RowMatShape=form.cleaned_data['R1_Row_Mat_Shape']).filter(
                        R1_RowMatType=form.cleaned_data['R1_Row_Mat_Type']).filter(
                        R1_MaterilUnit=form.cleaned_data['R1_Materil_Unit']).update(R1_MaterilQty=sto)

                    # obj2.save()
                else:
                    obj2.R1_RowMatSize = form.cleaned_data['R1_Row_Mat_Size']
                    obj2.R1_RowMatShape = form.cleaned_data['R1_Row_Mat_Shape']
                    obj2.R1_RowMatType = form.cleaned_data['R1_Row_Mat_Type']
                    obj2.R1_MaterilQty = form.cleaned_data['R1_Materil_Qty']
                    obj2.R1_MaterilUnit = form.cleaned_data['R1_Materil_Unit']
                    obj2.save()


                obj1.save()
                # form = Purchase_Entry()

                no = PurchaseRawMaterial.objects.count()
                print("Code is here1")

                form2 = RawMaterialDetail.objects.filter(R2_NO=no)
                data1 = PurchaseRawMaterial.objects.filter(R_No=no).first()
                data = {'R1_NO': data1.R_No, 'R1_Row_Mat_Size': "", 'R1_Row_Mat_Shape': "",
                        'R1_Row_Mat_Type': "", 'R1_Materil_Qty': "",
                        'R1_Materil_Unit': "", 'R1_Materil_Rate': "", 'amount': data1.R_Amount, 'R1_Date': data1.R_Date,
                        'R1_PO_NO': data1.R_PONO, 'Supplier': data1.supplier, 'inv_NO': data1.R_Invoice,
                        'inv_Date': data1.R_Inv_Date}
                form = Purchase_Entry(initial=data)
                # cleartext()
                return render(request, 'Purchase_entry.html', {'form': form, 'form2': form2})
            else:

                # R_No = models.IntegerField(default=number)
                # R_Date = models.DateTimeField(auto_now=True)
                # R_Invoice = models.IntegerField()
                # R_PONO = models.IntegerField()
                # R_Inv_Date = models.DateField()
                # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
                # R_Amount = models.DecimalField(decimal_places=2, max_digits=10000)
                supplier_name = form.cleaned_data['Supplier']
                supplier =  Supplier.objects.filter(SupplierName=supplier_name)[0]
                invoice_number =form.cleaned_data['inv_NO']
                obj.R_Invoice = form.cleaned_data['inv_NO']
                obj.R_PONO = form.cleaned_data['R1_PO_NO']
                obj.R_Inv_Date = form.cleaned_data['inv_Date']
                obj.supplier = supplier

                obj1.R2_RowMatSize = form.cleaned_data['R1_Row_Mat_Size']
                obj1.R2_RowMatShape = form.cleaned_data['R1_Row_Mat_Shape']
                obj1.R2_RowMatType = form.cleaned_data['R1_Row_Mat_Type']
                obj1.R2_MaterilQty = form.cleaned_data['R1_Materil_Qty']
                obj1.R2_MaterilUnit = form.cleaned_data['R1_Materil_Unit']
                obj1.R2_MaterilRates = form.cleaned_data['R1_Materil_Rate']
                total_amount = obj1.R2_MaterilRates * obj1.R2_MaterilQty
                obj1.R2_Total = total_amount


                obj.R_Amount = total_amount
                obj.save()
                obj1.R2_NO = PurchaseRawMaterial.objects.filter(supplier__SupplierName=supplier_name).last().R_No
                obj1.R2_Invoice = form.cleaned_data['inv_NO']


                no = PurchaseRawMaterial.objects.count()

                # amt = PurchaseRawMaterial.objects.filter(R_No=no).first().R_Amount
                # print("amt")
                # print(amt)
                # amt = amt + obj1.R2_Total

                if CuttingDetail.objects.filter(R1_RowMatSize=form.cleaned_data['R1_Row_Mat_Size']).filter(
                        R1_RowMatShape=form.cleaned_data['R1_Row_Mat_Shape']).filter(
                        R1_RowMatType=form.cleaned_data['R1_Row_Mat_Type']):
                    sto = CuttingDetail.objects.filter(R1_RowMatSize=form.cleaned_data['R1_Row_Mat_Size']).filter(
                        R1_RowMatShape=form.cleaned_data['R1_Row_Mat_Shape']).filter(
                        R1_RowMatType=form.cleaned_data['R1_Row_Mat_Type']).first().R1_MaterilQty

                    sto = sto + form.cleaned_data['R1_Materil_Qty']
                    print(sto)
                    CuttingDetail.objects.filter(R1_RowMatSize=form.cleaned_data['R1_Row_Mat_Size']).filter(
                        R1_RowMatShape=form.cleaned_data['R1_Row_Mat_Shape']).filter(
                        R1_RowMatType=form.cleaned_data['R1_Row_Mat_Type']).update(R1_MaterilQty=sto)



                else:
                    obj2.R1_RowMatSize = form.cleaned_data['R1_Row_Mat_Size']
                    obj2.R1_RowMatShape = form.cleaned_data['R1_Row_Mat_Shape']
                    obj2.R1_RowMatType = form.cleaned_data['R1_Row_Mat_Type']
                    obj2.R1_MaterilQty = form.cleaned_data['R1_Materil_Qty']
                    obj2.save()

                obj1.save()
                # obj.save()
                # form = Purchase_Entry()

                PurchaseRawMaterial.objects.filter(R_No=no).update(R_Amount=total_amount)
                print("Code is here2")
                form2 = RawMaterialDetail.objects.filter(R2_Invoice=form.cleaned_data['inv_NO'])
                data1 = PurchaseRawMaterial.objects.filter(R_No=no).first()
                data = {'R1_NO': data1.R_No, 'R1_Row_Mat_Size': "", 'R1_Row_Mat_Shape': "",
                        'R1_Row_Mat_Type': "", 'R1_Materil_Qty': "",
                        'R1_Materil_Unit': "", 'R1_Materil_Rate': "", 'amount': data1.R_Amount, 'R1_Date': data1.R_Date,
                        'R1_PO_NO': data1.R_PONO, 'Supplier': data1.supplier.SupplierName, 'inv_NO': data1.R_Invoice,
                        'inv_Date': data1.R_Inv_Date}
                form = Purchase_Entry(initial=data)

                final_amount = 0
                from django.db.models import Sum
                # final_amount = RawMaterialDetail.objects.filter(R2_Invoice=form.cleaned_data['inv_NO']).annotate(sum=Sum('R2_Total'))
                final_amount = RawMaterialDetail.objects.filter(R2_Invoice=invoice_number).aggregate(grand_total=Sum('R2_Total'))
                if(final_amount['grand_total']):
                    return render(request, 'Purchase_entry.html', {'form': form,'form2':form2 , 'final_amount':final_amount['grand_total']})
                else:
                    return render(request, 'Purchase_entry.html', {'form': form, 'form2': form2})
            # return http.HttpResponseRedirect('/Add_Supplier/')
            # return render(request, 'Supplier.html', {'form': form})
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Purchase_Entry()
        search_query = request.GET.get('search_box', None)
        number = PurchaseRawMaterial.objects.count()
        number = number + 1
        # print(number)
        form2 = RawMaterialDetail.objects.filter(R2_NO=number)

        print("Code is here3")
        return render(request, 'Purchase_entry.html', {'form': form, 'form2': form2})


def Stock_Details(request):
    form = CuttingDetail.objects.all().exclude(R1_MaterilQty=0)
    return render(request, 'stock_details.html', {'form': form})


def Cutting(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = sendcutting(request.POST)
        if form.is_valid():
            cd = form.cleaned_data['R4_Materil_Qty']
            ab = form.cleaned_data['R4_Materil_cut']
            ef = form.cleaned_data['R4_Row_Mat_Unit']
            xy = form.cleaned_data['id_cut']
            if ab <= cd:
                ff = cd - ab

                print("Pk is here")
                print(ef)
                CuttingDetail.objects.filter(id=xy).filter(R1_MaterilUnit=ef).update(R1_MaterilQty=ff)
                # form = CuttingDetail.objects.all()
                return redirect("/Home/Stock/")
            else:
                messages.error(request, 'Cutting Qty Can Not Be More that Stock Qty')
                # from = Login()
                pk = form.cleaned_data['id_cut']
                Cuttingfill = CuttingDetail.objects.filter(id=pk).first()
                print("Form is here")
                # print(form)
                data = {'R4_Row_Mat_Size': Cuttingfill.R1_RowMatSize, 'R4_Row_Mat_Shape': Cuttingfill.R1_RowMatShape,
                        'R4_Row_Mat_Type': Cuttingfill.R1_RowMatType, 'R4_Materil_Qty': Cuttingfill.R1_MaterilQty,
                        'id_cut': Cuttingfill.id, 'R4_Row_Mat_Unit': Cuttingfill.R1_MaterilUnit}
                form1 = sendcutting(initial=data)
                return render(request, 'cutting.html', {'form1': form1})

    else:
        pk = request.GET.get('pk')
        Cuttingfill = CuttingDetail.objects.filter(id=pk).first()
        print("Form is here")
        # print(form)
        data = {'R4_Row_Mat_Size': Cuttingfill.R1_RowMatSize, 'R4_Row_Mat_Shape': Cuttingfill.R1_RowMatShape,
                'R4_Row_Mat_Type': Cuttingfill.R1_RowMatType, 'R4_Materil_Qty': Cuttingfill.R1_MaterilQty,
                'id_cut': Cuttingfill.id, 'R4_Row_Mat_Unit': Cuttingfill.R1_MaterilUnit}
        form1 = sendcutting(initial=data)
        return render(request, 'cutting.html', {'form1': form1})


def Purchase_Print(request):
    pk = request.GET.get('pk')
    print("primary key", pk)
    Cuttingfill = PurchaseOrder.objects.all().filter(PONO=pk).first()
    print("Form is here")
    # print(form)
    data = {'PO_NO': Cuttingfill.PONO, 'PO_Date': Cuttingfill.PODate, 'Supplier': Cuttingfill.supplier}
    # form = PurchaseOrder.objects.all().filter(PONO=pk)
    form = Purchase_Order(initial=data)
    # form4= form.cleaned_data['PO_NO']

    # number=PurchaseOrder.objects.count()
    # number=number + 1
    # print(number)
    form2 = PurchaseDetail.objects.all().filter(PONO=pk)
    print("Code is hew", form2)
    return render(request, 'PO_Print.html', {'form': form, 'form2': form2})
