# Generated by Django 3.2.6 on 2024-12-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('total_facturas', models.IntegerField()),
                ('detalle_facturas', models.JSONField()),
                ('fecha_generacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'reportes',
            },
        ),
    ]
