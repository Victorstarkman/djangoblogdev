# Generated by Django 2.2 on 2021-06-08 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombre de la Categoría')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoría Activada/Categoría no Activada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='fecha de Creacíon')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
