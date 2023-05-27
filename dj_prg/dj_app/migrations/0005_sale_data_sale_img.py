# Generated by Django 4.1.5 on 2023-05-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_app', '0004_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='data',
            field=models.DateField(null=True, verbose_name='Дата публикации акции'),
        ),
        migrations.AddField(
            model_name='sale',
            name='img',
            field=models.ImageField(default='img.pgn', upload_to='sale/', verbose_name='Изображение акции'),
            preserve_default=False,
        ),
    ]
