# Generated by Django 3.0.7 on 2020-07-04 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20200704_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilities',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]
