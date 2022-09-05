# Generated by Django 4.1 on 2022-09-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuariosRegistro',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('correo', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='motivo',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='observaciones',
            field=models.CharField(max_length=200),
        ),
    ]