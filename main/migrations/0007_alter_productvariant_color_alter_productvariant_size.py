# Generated by Django 4.1.3 on 2023-01-03 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_color_image_alter_color_title_alter_size_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.color'),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.size'),
        ),
    ]
