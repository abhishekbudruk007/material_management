"""Gorson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from Purchase import views , apis

urlpatterns = [
    path('',views.Login, name='Login'),
    path('Login/', views.Login, name='Login'),
    path('Home/',views.Home, name='home'),
    path('admin/', admin.site.urls),
    path('Home/Add_Supplier/',views.Supplier_name, name='Add_Supplier'),
    path('Home/Purchase_Order/',views.Purchase_Material, name='Purchase_Order'),
    path('Home/Purchase_Entry/',views.add_purchase, name='Purchase_Entry'),
    path('Home/Stock/',views.Stock_Details, name='Stock'),
    path('Home/Stock/Cutting/',views.Cutting, name='Home/Stock/Cutting/'),
    path('Home/Purchase_Order/Purchase_Print/',views.Purchase_Print, name='Purchase_Order_Print'),
    path('Home/logout/', views.Logout, name='logout'),

    #All API's
    path('api/get_suppliers', apis.GetSuppliers.as_view(), name='get_suppliers'),
    path('api/get_stock_details', apis.GetStockDetails.as_view(), name='get_stock_details')

]
