# Generated by Django 4.0.2 on 2022-02-25 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BreedUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url0', models.URLField(max_length=256)),
                ('url1', models.URLField(max_length=256)),
                ('url2', models.URLField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Racas',
            fields=[
                ('id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=256)),
                ('origem', models.CharField(max_length=256)),
                ('temperamento', models.CharField(max_length=256)),
                ('descricao', models.CharField(max_length=256)),
            ],
        ),
    ]