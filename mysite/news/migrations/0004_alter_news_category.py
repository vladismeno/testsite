# Generated by Django 5.0.2 on 2024-03-05 03:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_categories_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='news.categories', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
