# Generated by Django 3.2.13 on 2022-05-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20220512_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
