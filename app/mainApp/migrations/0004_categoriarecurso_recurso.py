# Generated by Django 3.1.1 on 2020-11-09 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20201109_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaRecurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoria_recurso',
                'verbose_name_plural': 'categoria_recursos',
            },
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(blank=True, max_length=400, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='noticias')),
                ('archivo', models.FileField(upload_to='archivos')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('categorias', models.ManyToManyField(to='mainApp.CategoriaRecurso')),
            ],
            options={
                'verbose_name': 'recurso',
                'verbose_name_plural': 'recursos',
            },
        ),
    ]
