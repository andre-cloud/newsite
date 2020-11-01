# Generated by Django 3.1.1 on 2020-10-30 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0003_argomento_materia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esercizio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Inserire un titolo esplicativo', max_length=120)),
                ('text', models.TextField(help_text='Scrivere il testo del problema. Se si è utilizzato il bot che sfrutta la tecnologia OCR controllare la correttezza del teso ricevuto.')),
                ('fig', models.ImageField(blank=True, help_text="Carica un'eventuale immagine che completi il testo dell'esercizio", null=True, upload_to='img/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('referance', models.TextField(help_text='Se è un libro: Cognome N., Titolo del testo, Casa editrice, anno di pubblicazione con edizione, pagina. Se è un sito inserire il link')),
                ('status', models.CharField(default='Draft', editable=False, max_length=10)),
                ('slug', models.SlugField(help_text='NON MODIFICARE a meno di omonimia')),
                ('argomento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercises.argomento')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercises.materia')),
            ],
            options={
                'verbose_name': 'Esercizio',
                'verbose_name_plural': 'Esercizi',
            },
        ),
        migrations.RemoveField(
            model_name='chimica_generale_analitica',
            name='exercise_ptr',
        ),
        migrations.RemoveField(
            model_name='chimica_organica',
            name='exercise_ptr',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='matematica',
            name='exercise_ptr',
        ),
        migrations.DeleteModel(
            name='Chimica_Fisica',
        ),
        migrations.DeleteModel(
            name='Chimica_Generale_Analitica',
        ),
        migrations.DeleteModel(
            name='Chimica_Organica',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='Matematica',
        ),
    ]