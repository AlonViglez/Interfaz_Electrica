# Generated by Django 5.0.2 on 2024-03-25 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('materia', models.CharField(max_length=30)),
                ('numero_cuenta', models.IntegerField(max_length=9)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]