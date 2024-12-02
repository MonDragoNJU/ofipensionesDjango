# Generated by Django 3.2.6 on 2024-12-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estudiante', models.IntegerField()),
                ('institucion_asociada', models.IntegerField()),
                ('responsable_economico', models.IntegerField()),
                ('fecha_limite_pago', models.DateField()),
                ('fecha_inicial', models.DateField()),
                ('valor', models.FloatField()),
            ],
            options={
                'db_table': 'facturas',
            },
        ),
    ]