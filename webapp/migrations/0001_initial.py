# Generated by Django 5.1.6 on 2025-02-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=2500)),
                ('last_name', models.CharField(max_length=2500)),
                ('phone', models.IntegerField()),
                ('tall', models.IntegerField()),
                ('wedgit', models.IntegerField()),
                ('adrees', models.CharField(max_length=500)),
                ('create_at', models.DateField()),
            ],
        ),
    ]
