# Generated by Django 4.0 on 2022-11-23 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_childdata_birth_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='childdata',
            name='birth_certificate',
            field=models.FileField(blank=True, null=True, upload_to='childdata'),
        ),
    ]
