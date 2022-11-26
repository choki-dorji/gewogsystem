# Generated by Django 4.0 on 2022-11-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_childdata_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='childdata',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=None, max_length=100),
            preserve_default=False,
        ),
    ]