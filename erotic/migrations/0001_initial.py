# Generated by Django 2.1.7 on 2019-02-21 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SexyActress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('memo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('url', models.CharField(max_length=300)),
                ('memo', models.TextField()),
                ('sexyActress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='erotic.SexyActress')),
            ],
        ),
    ]