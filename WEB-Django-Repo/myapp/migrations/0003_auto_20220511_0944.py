# Generated by Django 3.2.13 on 2022-05-11 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_student_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='x',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]