# Generated by Django 4.2 on 2023-04-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
