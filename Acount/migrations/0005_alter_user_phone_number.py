# Generated by Django 4.1 on 2022-08-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount', '0004_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
