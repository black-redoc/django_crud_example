# Generated by Django 3.0.11 on 2021-01-14 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('priority', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1, verbose_name='Prioridad')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
            ],
        ),
    ]
