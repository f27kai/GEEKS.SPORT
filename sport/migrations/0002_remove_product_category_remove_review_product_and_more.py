# Generated by Django 5.0.6 on 2024-06-25 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
