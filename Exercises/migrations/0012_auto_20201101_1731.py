# Generated by Django 3.1.1 on 2020-11-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0011_auto_20201031_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='argomento',
            name='descrizione',
        ),
        migrations.AlterField(
            model_name='immaginiteoria',
            name='image',
            field=models.ImageField(upload_to='img_theo/'),
        ),
    ]
