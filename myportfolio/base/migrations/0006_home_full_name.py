# Generated by Django 3.1.4 on 2021-01-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='full_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Full name'),
        ),
    ]
