# Generated by Django 5.1.2 on 2024-10-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=225, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=225, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]