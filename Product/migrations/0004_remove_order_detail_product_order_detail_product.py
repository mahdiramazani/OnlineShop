# Generated by Django 4.0.6 on 2022-07-30 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_order_order_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_detail',
            name='product',
        ),
        migrations.AddField(
            model_name='order_detail',
            name='product',
            field=models.ManyToManyField(related_name='product', to='Product.product'),
        ),
    ]
