# Generated by Django 3.1.4 on 2021-01-16 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210115_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='logo_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Your Logo picture: File type: "jpg or png"'),
        ),
    ]
