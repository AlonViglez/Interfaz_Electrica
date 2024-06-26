# Generated by Django 5.0.2 on 2024-04-15 17:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_alter_usuario_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('materia', models.CharField(max_length=30)),
                ('especialidad', models.CharField(max_length=50)),
                ('numero_cuenta', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
