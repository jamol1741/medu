# Generated by Django 3.2 on 2021-06-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, to='educations.CourseTag'),
        ),
        migrations.AlterField(
            model_name='education',
            name='teachers',
            field=models.ManyToManyField(blank=True, to='educations.Teacher'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='certificates',
            field=models.ManyToManyField(blank=True, to='educations.Certificate'),
        ),
    ]
