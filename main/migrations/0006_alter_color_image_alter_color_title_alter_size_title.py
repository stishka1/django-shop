# Generated by Django 4.1.3 on 2023-01-03 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_productvariant_color_alter_productvariant_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Иконка цвета'),
        ),
        migrations.AlterField(
            model_name='color',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='size',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Размер'),
        ),
    ]
