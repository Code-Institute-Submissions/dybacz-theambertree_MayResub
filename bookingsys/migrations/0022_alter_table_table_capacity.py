# Generated by Django 3.2 on 2022-02-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsys', '0021_alter_table_table_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='table_capacity',
            field=models.IntegerField(default=1),
        ),
    ]
