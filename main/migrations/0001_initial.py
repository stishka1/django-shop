# Generated by Django 4.1.3 on 2022-12-07 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ban_imgs/', verbose_name='Баннер')),
                ('alt_text', models.CharField(max_length=200, verbose_name='Текст ALT')),
            ],
            options={
                'verbose_name_plural': '5. Баннеры',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Бренд')),
                ('image', models.ImageField(upload_to='brand_imgs/', verbose_name='Лого бренда')),
            ],
            options={
                'verbose_name_plural': '4. Бренды',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Категория')),
                ('image', models.ImageField(upload_to='cat_imgs/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name_plural': '3. Категории',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Цвет')),
                ('image', models.CharField(max_length=100, verbose_name='Иконка цвета')),
            ],
            options={
                'verbose_name_plural': '6. Цвета',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('sku', models.CharField(default='DEFAULT', max_length=40, verbose_name='Артикул')),
                ('video', models.CharField(blank=True, max_length=300, verbose_name='Видео')),
                ('preview_desc', models.TextField(max_length=200, null=True, verbose_name='Анонс')),
                ('detail_desc', models.TextField(verbose_name='Описание')),
                ('slug', models.CharField(max_length=400, verbose_name='ЧПУ')),
                ('specs', models.TextField(blank=True, verbose_name='Характеристики')),
                ('active', models.BooleanField(default=True, verbose_name='Активность')),
                ('in_stock', models.BooleanField(default=True, verbose_name='Наличие на складе')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('popularity', models.PositiveIntegerField(blank=True, null=True, verbose_name='Популярность')),
                ('is_featured', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.color')),
            ],
            options={
                'verbose_name_plural': '1. Товары',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Размер')),
            ],
            options={
                'verbose_name_plural': '7. Размеры',
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='product_imgs/', verbose_name='Картинка 1')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='product_imgs/', verbose_name='Картинка 2')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='product_imgs/', verbose_name='Картинка 3')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='product_imgs/', verbose_name='Картинка 4')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='product_imgs/', verbose_name='Картинка 5')),
                ('price', models.PositiveIntegerField(verbose_name='Розничная цена')),
                ('old_price', models.FloatField(blank=True, default=0.0, verbose_name='Старая цена')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.size')),
            ],
            options={
                'verbose_name_plural': '2. Варианты товаров',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.size'),
        ),
    ]
