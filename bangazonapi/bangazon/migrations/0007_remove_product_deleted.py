# Generated by Django 3.0.3 on 2020-03-06 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon', '0006_auto_20200306_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='deleted',
        ),
    ]