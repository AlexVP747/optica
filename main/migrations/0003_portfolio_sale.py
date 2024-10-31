# Generated by Django 5.1 on 2024-10-31 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_order_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originalfoto', models.ImageField(upload_to='image', verbose_name='фото')),
                ('text', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'наша акция',
                'verbose_name_plural': 'наши акции',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originalfoto', models.ImageField(upload_to='image', verbose_name='фото')),
                ('text', models.TextField(verbose_name=' акции')),
            ],
        ),
    ]