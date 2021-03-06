# Generated by Django 3.1.4 on 2021-02-01 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20210130_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_class', models.CharField(max_length=200, null=True, verbose_name='Your service  class for Feathericon class')),
                ('service_name', models.TextField(max_length=2000, null=True, verbose_name='Your service name')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_title_main', models.CharField(max_length=255, null=True, verbose_name='Your services main Title')),
                ('services_title', models.TextField(max_length=10000, null=True, verbose_name='Your services detail')),
            ],
        ),
        migrations.RemoveField(
            model_name='resultoutcome',
            name='result_class',
        ),
    ]
