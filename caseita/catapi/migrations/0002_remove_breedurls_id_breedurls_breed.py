# Generated by Django 4.0.2 on 2022-02-25 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breedurls',
            name='id',
        ),
        migrations.AddField(
            model_name='breedurls',
            name='breed',
            field=models.CharField(default='', max_length=256, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
