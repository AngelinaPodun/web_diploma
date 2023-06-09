# Generated by Django 4.1.5 on 2023-05-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_app', '0008_comments_date_alter_post_promo_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя заказчика')),
                ('phone', models.CharField(max_length=13, verbose_name='Номер телефона заказчика')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='Email заказчика')),
                ('choices', models.ManyToManyField(to='dj_app.servicecategory')),
            ],
        ),
    ]
