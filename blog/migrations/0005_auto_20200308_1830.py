# Generated by Django 2.2.11 on 2020-03-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200307_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email_id',
            field=models.EmailField(default='', max_length=40),
        ),
    ]
