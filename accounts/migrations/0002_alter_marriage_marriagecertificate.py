# Generated by Django 4.0 on 2022-11-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marriage',
            name='MarriageCertificate',
            field=models.FileField(null=True, upload_to='file'),
        ),
    ]
