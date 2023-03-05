# Generated by Django 4.1.7 on 2023-03-04 10:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora de la creación del objeto.', verbose_name='Fecha de creación')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora de la última modificación del objeto.', verbose_name='Fecha de modificación')),
                ('cookie', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('coins', models.IntegerField(default=5000, verbose_name='Monedas')),
                ('products', models.ManyToManyField(blank=True, related_name='buyer', to='products.product', verbose_name='Productos comprados')),
            ],
            options={
                'verbose_name': 'Comprador',
                'verbose_name_plural': 'Compradores',
                'ordering': ['cookie'],
            },
        ),
    ]
