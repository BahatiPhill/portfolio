# Generated by Django 2.1.5 on 2019-01-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190114_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogarticles',
            name='title_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/title_images/'),
        ),
    ]
