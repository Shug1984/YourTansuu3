# Generated by Django 3.2.8 on 2021-11-02 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['item_name']},
        ),
        migrations.AlterField(
            model_name='item',
            name='closet',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='contents.closet'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_brand',
            field=models.ForeignKey(blank=True, db_column='item_brand', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.itembrand', verbose_name='ブランド名称'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_color',
            field=models.ForeignKey(blank=True, db_column='item_color', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.itemcolor', verbose_name='アイテムカラー'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(db_column='item_type', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.itemtype', verbose_name='アイテム種類'),
        ),
        migrations.AlterField(
            model_name='item',
            name='purchase_place',
            field=models.ForeignKey(blank=True, db_column='purchase_place', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.purchaseplace', verbose_name='購入場所'),
        ),
        migrations.AlterField(
            model_name='itembrand',
            name='item_brand',
            field=models.CharField(max_length=155, unique=True, verbose_name='ブランド'),
        ),
        migrations.AlterField(
            model_name='itemcolor',
            name='item_color',
            field=models.CharField(max_length=100, unique=True, verbose_name='アイテムカラー'),
        ),
        migrations.AlterField(
            model_name='itemtype',
            name='item_type',
            field=models.CharField(max_length=155, unique=True, verbose_name='アイテム種類'),
        ),
        migrations.AlterField(
            model_name='purchaseplace',
            name='purchase_place',
            field=models.CharField(max_length=155, unique=True, verbose_name='購入場所'),
        ),
    ]
