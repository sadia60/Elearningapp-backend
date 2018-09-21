# Generated by Django 2.1.1 on 2018-09-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auther_name', models.CharField(max_length=50)),
                ('course_title', models.CharField(max_length=50)),
                ('course_description', models.CharField(max_length=100)),
                ('course_created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('course_updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]