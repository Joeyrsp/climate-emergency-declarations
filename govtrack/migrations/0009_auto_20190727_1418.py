# Generated by Django 2.2.3 on 2019-07-27 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("govtrack", "0008_auto_20190725_1024"),
    ]

    operations = [
        migrations.AlterField(
            model_name="node",
            name="supplements",
            field=models.ManyToManyField(
                blank=True, related_name="supplement", to="govtrack.Node"
            ),
        ),
    ]
