# Generated by Django 4.2 on 2023-04-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Beverages', 'Beverages')], default='Breakfast', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
