# Generated by Django 4.2.7 on 2024-03-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0002_registration_pg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_pg',
            name='Mobile_number',
            field=models.CharField(max_length=10),
        ),
    ]