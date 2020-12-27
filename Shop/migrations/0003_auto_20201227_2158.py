# Generated by Django 3.1.1 on 2020-12-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_shop_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='link_cover',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='link_felpa',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='link_tshirt',
        ),
        migrations.AddField(
            model_name='shop',
            name='slug',
            field=models.SlugField(default='design-prova'),
            preserve_default=False,
        ),
    ]
