# Generated by Django 3.1.4 on 2021-01-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_home_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=100, null=True, verbose_name='Social name')),
                ('social_class', models.CharField(max_length=255, null=True, verbose_name='Social icon for  MDI class')),
                ('social_link', models.CharField(max_length=255, null=True, verbose_name='Social Link')),
            ],
        ),
    ]
