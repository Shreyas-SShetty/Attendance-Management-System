# Generated by Django 2.2.11 on 2020-03-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200317_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
