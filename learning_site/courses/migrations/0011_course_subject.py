# Generated by Django 2.0.3 on 2018-05-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.CharField(default='', max_length=100),
        ),
    ]