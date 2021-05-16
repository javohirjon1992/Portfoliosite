# Generated by Django 3.1.4 on 2021-02-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_profession_workexpertise_yourskills'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexpertise',
            name='work_image',
            field=models.ImageField(blank=True, null=True, upload_to='workpicture/', verbose_name='Your work picture: File type: "jpg or png": Size 1100x1650 pixels'),
        ),
    ]