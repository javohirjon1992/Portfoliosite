# Generated by Django 3.1.4 on 2021-02-01 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_auto_20210201_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='workpartdetail',
            name='complete_projects',
            field=models.TextField(max_length=1500, null=True, verbose_name='Write in detail about the projects you have completed'),
        ),
    ]
