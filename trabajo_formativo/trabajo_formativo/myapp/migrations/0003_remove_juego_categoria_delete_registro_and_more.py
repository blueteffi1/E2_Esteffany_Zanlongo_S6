# Generated by Django 5.0.3 on 2024-04-10 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_registro_alter_juego_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='registro',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Juego',
        ),
    ]
