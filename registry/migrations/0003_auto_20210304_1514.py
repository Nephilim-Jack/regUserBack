# Generated by Django 3.1.7 on 2021-03-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_auto_20210304_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cep',
            field=models.IntegerField(blank=True, null=True, verbose_name='cep'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='complement',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='complement'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='street',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='street'),
        ),
    ]
