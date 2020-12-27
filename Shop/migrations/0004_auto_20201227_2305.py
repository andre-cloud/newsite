# Generated by Django 3.1.1 on 2020-12-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_auto_20201227_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='status',
        ),
        migrations.AddField(
            model_name='shop',
            name='donna_felpa',
            field=models.CharField(blank=True, help_text='Inserisci il link per la felpa donna', max_length=2000),
        ),
        migrations.AddField(
            model_name='shop',
            name='donna_tshirt',
            field=models.CharField(blank=True, help_text='Inserisci il link per la t-shirt donna', max_length=2000),
        ),
        migrations.AddField(
            model_name='shop',
            name='unisex_felpa',
            field=models.CharField(blank=True, help_text='Inserisci il link per la felpa unisex', max_length=2000),
        ),
        migrations.AddField(
            model_name='shop',
            name='unisex_tshirt',
            field=models.CharField(blank=True, help_text='Inserisci il link per la t-shirt unisex', max_length=2000),
        ),
        migrations.AddField(
            model_name='shop',
            name='uomo_felpa',
            field=models.CharField(blank=True, help_text='Inserisci il link per la felpa uomo', max_length=2000),
        ),
        migrations.AddField(
            model_name='shop',
            name='uomo_tshirt',
            field=models.CharField(blank=True, help_text='Inserisci il link per la t-shirt uomo', max_length=2000),
        ),
    ]
