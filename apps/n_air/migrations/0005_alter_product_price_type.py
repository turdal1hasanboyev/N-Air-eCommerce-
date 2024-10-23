# Generated by Django 5.1.2 on 2024-10-23 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n_air', '0004_alter_product_price_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_type',
            field=models.CharField(blank=True, choices=[('UZS', 'UZB'), ('$', 'USA'), ('€', 'EURO'), ('₽', 'RUS')], db_default='UZB', max_length=225, null=True),
        ),
    ]
