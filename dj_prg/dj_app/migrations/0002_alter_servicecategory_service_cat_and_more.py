# Generated by Django 4.1.5 on 2023-05-10 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dj_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='service_cat',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='dj_app.service', verbose_name='Выбрать категорию услуг'),
        ),
        migrations.AlterField(
            model_name='theservice',
            name='service',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='dj_app.servicecategory', verbose_name='Выбрать подкатегорию услуг'),
        ),
    ]
