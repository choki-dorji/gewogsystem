# Generated by Django 4.0 on 2022-11-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_childdata_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childdata',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=None, max_length=100, null=True),
        ),
    ]
