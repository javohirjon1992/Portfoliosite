# Generated by Django 3.1.4 on 2021-01-29 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210116_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_skills', models.CharField(max_length=255, null=True, verbose_name='Skills')),
                ('about_us', models.TextField(max_length=1000, null=True, verbose_name='About my skills')),
                ('home_picture', models.ImageField(blank=True, null=True, upload_to='homeimages/', verbose_name='Your picture: File type: "jpg or png"')),
                ('your_cv', models.FileField(blank=True, null=True, upload_to='cv/', verbose_name='Your CV: File type: "pdf or doc"')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
