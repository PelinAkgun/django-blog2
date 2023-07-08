# Generated by Django 3.1.5 on 2023-07-08 07:39

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230708_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategorimodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='isim', unique=True),
        ),
        migrations.AlterModelTable(
            name='kategorimodel',
            table='kategori',
        ),
    ]