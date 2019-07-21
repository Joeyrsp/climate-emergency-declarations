# Generated by Django 2.2.3 on 2019-07-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('govtrack', '0005_auto_20190719_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='parent',
        ),
        migrations.AddField(
            model_name='node',
            name='parents',
            field=models.ManyToManyField(to='govtrack.Node'),
        ),
    ]
