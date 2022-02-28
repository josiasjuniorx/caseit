# Generated by Django 4.0.2 on 2022-02-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catapi', '0003_rename_breed_breedurls_breedid'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryUrls',
            fields=[
                ('categoryid', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('categoryname', models.CharField(max_length=256)),
                ('url0', models.URLField(max_length=256)),
                ('url1', models.URLField(max_length=256)),
                ('url2', models.URLField(max_length=256)),
            ],
        ),
    ]
