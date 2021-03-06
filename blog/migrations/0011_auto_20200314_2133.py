# Generated by Django 2.2.11 on 2020-03-14 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_attendance_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'verbose_name': 'attendance'},
        ),
        migrations.AddField(
            model_name='attendance',
            name='instructor_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Instructor'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Student'),
        ),
    ]
