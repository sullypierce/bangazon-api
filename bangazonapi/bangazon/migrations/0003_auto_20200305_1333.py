# Generated by Django 3.0.3 on 2020-03-05 19:33

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon', '0002_auto_20200221_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='paymenttype',
            options={'ordering': (django.db.models.expressions.OrderBy(django.db.models.expressions.F('expiration_date'), descending=True),), 'verbose_name': ('payment_type',), 'verbose_name_plural': ('payment_types',)},
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='paymenttype',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bangazon.PaymentType'),
        ),
        migrations.AlterField(
            model_name='paymenttype',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bangazon.Customer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazon.ProductType'),
        ),
    ]
