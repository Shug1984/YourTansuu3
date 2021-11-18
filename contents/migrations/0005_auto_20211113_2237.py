# Generated by Django 3.2.8 on 2021-11-13 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_auto_20211113_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='closet',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='contents.closet'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_brand',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='contents.itembrand'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_color',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='contents.itemcolor'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='contents.itemtype'),
        ),
        migrations.AlterField(
            model_name='item',
            name='purchase_place',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='contents.purchaseplace'),
        ),
    ]
