# Generated by Django 2.2 on 2019-06-18 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20190616_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='static/img/Arcadia64.jpg', upload_to='profile_img'),
        ),
    ]
