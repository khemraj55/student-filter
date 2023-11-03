# Generated by Django 4.2.7 on 2023-11-01 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_no', models.IntegerField(unique=True)),
                ('subject1', models.CharField(max_length=100)),
                ('subject2', models.CharField(max_length=100)),
                ('subject3', models.CharField(max_length=100)),
                ('subject4', models.CharField(max_length=100)),
                ('subject5', models.CharField(max_length=100)),
                ('score1', models.IntegerField()),
                ('score2', models.IntegerField()),
                ('score3', models.IntegerField()),
                ('score4', models.IntegerField()),
                ('score5', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('class_name', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
            ],
        ),
    ]