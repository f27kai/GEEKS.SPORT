# Generated by Django 5.0.6 on 2024-06-26 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_remove_product_category_remove_review_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouTube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_youtube', models.URLField(verbose_name='Ссылка на ютуб')),
            ],
        ),
    ]
