# Generated by Django 3.2 on 2022-02-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsys', '0019_auto_20220210_1603'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ['-table_id']},
        ),
        migrations.RemoveField(
            model_name='table',
            name='table_name',
        ),
        migrations.AddField(
            model_name='table',
            name='table_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_capacity',
            field=models.IntegerField(default=1),
        ),
    ]
