# Generated by Django 5.1 on 2024-08-21 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
