# Generated by Django 3.1.1 on 2020-10-30 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0002_exercise_polymorphic_ctype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(help_text='Inserire il titolo della materia', max_length=250)),
                ('descrizione', models.TextField(help_text='Scrivere una minima descrizione per spiegare BREVEMENTE la materia')),
            ],
        ),
        migrations.CreateModel(
            name='Argomento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('argomento', models.CharField(help_text="Inserire il titolo dell'argomento", max_length=250)),
                ('descrizione', models.TextField(blank=True, help_text="Scrivere una minima descrizione per l'argomento")),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercises.materia')),
            ],
        ),
    ]