# Generated by Django 3.2.12 on 2022-02-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20220226_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email_id',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
        migrations.RemoveField(
            model_name='customer',
            name='product',
        ),
        migrations.AddField(
            model_name='customer',
            name='product',
            field=models.ManyToManyField(blank=True, to='item.Product'),
        ),
    ]
