# Generated by Django 4.0.2 on 2022-02-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catapi', '0005_remove_breedurls_url0_remove_breedurls_url1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breedurls',
            name='urls',
            field=models.JSONField(max_length=256),
        ),
    ]