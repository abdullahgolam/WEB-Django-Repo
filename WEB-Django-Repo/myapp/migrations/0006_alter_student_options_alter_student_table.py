# Generated by Django 4.0.4 on 2022-05-14 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20220512_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelTable(
            name='student',
            table=None,
        ),
    ]
