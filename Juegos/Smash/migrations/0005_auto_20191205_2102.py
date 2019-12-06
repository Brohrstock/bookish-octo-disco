# Generated by Django 2.2.7 on 2019-12-06 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smash', '0004_auto_20191205_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_noticia', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
