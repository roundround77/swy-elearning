# Generated by Django 4.0.8 on 2024-02-20 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_student_level'),
        ('course', '0010_alter_course_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakenCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_courses', to='course.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
        ),
    ]
