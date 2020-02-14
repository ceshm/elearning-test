# Generated by Django 3.0.3 on 2020-02-12 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='dependencies',
            field=models.ManyToManyField(blank=True, null=True, to='courses.Course'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='dependencies',
            field=models.ManyToManyField(blank=True, null=True, to='courses.Lesson'),
        ),
    ]
