# Generated by Django 2.0.6 on 2020-08-28 21:49

import Purchase.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CuttingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R1_RowMatSize', models.CharField(max_length=20)),
                ('R1_RowMatShape', models.CharField(max_length=20)),
                ('R1_RowMatType', models.CharField(max_length=20)),
                ('R1_MaterilQty', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('R1_MaterilUnit', models.CharField(default='KG', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PONO', models.IntegerField()),
                ('RowMatSize', models.CharField(max_length=20)),
                ('RowMatShape', models.CharField(max_length=20)),
                ('RowMatType', models.CharField(max_length=20)),
                ('MaterilQty', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('MaterilUnit', models.CharField(max_length=20)),
                ('MaterilRates', models.DecimalField(decimal_places=2, max_digits=10000)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PONO', models.IntegerField(default=Purchase.models.PurchaseOrder.number)),
                ('PODate', models.DateTimeField(auto_now=True)),
                ('Amount', models.DecimalField(decimal_places=2, default=0, max_digits=10000)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRawMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_No', models.IntegerField(default=Purchase.models.PurchaseRawMaterial.number)),
                ('R_Date', models.DateTimeField(auto_now=True)),
                ('R_Invoice', models.IntegerField()),
                ('R_PONO', models.IntegerField()),
                ('R_Inv_Date', models.DateField()),
                ('R_Amount', models.DecimalField(decimal_places=2, max_digits=10000)),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterialDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R2_NO', models.IntegerField()),
                ('R2_RowMatSize', models.CharField(max_length=20)),
                ('R2_RowMatShape', models.CharField(max_length=20)),
                ('R2_RowMatType', models.CharField(max_length=20)),
                ('R2_MaterilQty', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('R2_MaterilUnit', models.CharField(max_length=20)),
                ('R2_MaterilRates', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('R2_Total', models.DecimalField(decimal_places=2, max_digits=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Rawtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Row_Mat_Type', models.CharField(default='pipe', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Row_Mat_Shape', models.CharField(default='pipe', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SupplierName', models.CharField(max_length=100)),
                ('SupplierType', models.CharField(max_length=30)),
                ('SupplierAddress', models.CharField(max_length=500)),
                ('SupplierContact', models.IntegerField()),
                ('SupplierGST', models.CharField(max_length=15)),
                ('SupplierEMail', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Supplier_Type', models.CharField(default='INTERSTATE', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_Name', models.CharField(default='KG', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='purchaserawmaterial',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Purchase.Supplier'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Purchase.Supplier'),
        ),
    ]
