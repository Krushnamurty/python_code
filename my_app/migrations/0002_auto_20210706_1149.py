# Generated by Django 3.2.4 on 2021-07-06 06:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default=None, max_length=225)),
                ('created_at', models.CharField(default=datetime.datetime(2021, 7, 6, 11, 48, 58, 926583), max_length=225)),
                ('updated_by', models.CharField(default=datetime.datetime(2021, 7, 6, 11, 48, 58, 926583), max_length=225)),
                ('created_by', models.CharField(default='Rahit', max_length=225)),
            ],
            options={
                'db_table': 'Projects',
            },
        ),
        migrations.AlterField(
            model_name='clients',
            name='created_at',
            field=models.CharField(default=datetime.datetime(2021, 7, 6, 11, 48, 58, 926583), max_length=225),
        ),
        migrations.AlterField(
            model_name='clients',
            name='created_by',
            field=models.CharField(default='Rahit', max_length=225),
        ),
        migrations.AlterField(
            model_name='clients',
            name='update_at',
            field=models.CharField(default=datetime.datetime(2021, 7, 6, 11, 48, 58, 926583), max_length=225),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.projects')),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.AddField(
            model_name='projects',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.clients'),
        ),
    ]