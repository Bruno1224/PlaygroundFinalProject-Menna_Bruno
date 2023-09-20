# Generated by Django 4.0.5 on 2022-06-17 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaming', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gaming',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='gaming',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='gaming',
            name='platform',
            field=models.CharField(max_length=40, verbose_name='Plataforma'),
        ),
    ]