# Generated by Django 3.1.5 on 2023-07-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_iletisimmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yorummodel',
            name='guncellenme_tarihi',
        ),
        migrations.AddField(
            model_name='yorummodel',
            name='duzenlenme_tarihi',
            field=models.DateTimeField(auto_now=True),
        ),
    ]