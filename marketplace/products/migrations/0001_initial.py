# Generated by Django 4.1.7 on 2023-03-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora de la creación del objeto.', verbose_name='Fecha de creación')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora de la última modificación del objeto.', verbose_name='Fecha de modificación')),
                ('name', models.CharField(max_length=500, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen')),
                ('price', models.FloatField(default=0, verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['name'],
            },
        ),
    ]
