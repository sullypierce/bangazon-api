# Generated by Django 3.0.3 on 2020-03-09 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon', '0008_merge_20200309_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bangazon.ProductType'),
        ),
    ]
