# Generated by Django 3.1.1 on 2020-11-09 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_categoriarecurso_recurso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurso',
            name='imagen',
        ),
        migrations.AddField(
            model_name='recurso',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='archivo',
            field=models.FileField(upload_to='recursos'),
        ),
    ]