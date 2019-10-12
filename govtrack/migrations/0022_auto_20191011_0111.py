# Generated by Django 2.2.5 on 2019-10-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('govtrack', '0021_importdeclaration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declaration',
            name='status',
            field=models.CharField(choices=[('D', 'Declared'), ('N', 'Inactive'), ('R', 'Rejected'), ('V', 'Revoked'), ('P', 'In Progress'), ('J', 'Listing Rejected'), ('U', 'Listing Under Review')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='popcount',
            name='status',
            field=models.CharField(choices=[('D', 'Declared'), ('N', 'Inactive'), ('R', 'Rejected'), ('V', 'Revoked'), ('P', 'In Progress'), ('J', 'Listing Rejected'), ('U', 'Listing Under Review')], default='D', max_length=1),
        ),
    ]
