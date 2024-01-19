# Generated by Django 5.0 on 2023-12-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsumicenter', '0003_guadañas'),
    ]

    operations = [
        migrations.CreateModel(
            name='fumigadoras',
            fields=[
                ('id_fumigadora', models.AutoField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('Fecha_ingreso', models.DateField()),
                ('precio', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'db_table': 'fumigadoras',
            },
        ),
    ]
