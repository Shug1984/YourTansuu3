# Generated by Django 3.2.8 on 2021-10-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='personal_image',
            field=models.ImageField(upload_to='media/account', verbose_name='画像'),
        ),
    ]
