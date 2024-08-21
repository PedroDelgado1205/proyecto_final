# Generated by Django 5.1 on 2024-08-16 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=100)),
                ('ano_publicacion', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('portada', models.ImageField(blank=True, null=True, upload_to='portadas_libros/')),
            ],
        ),
    ]
