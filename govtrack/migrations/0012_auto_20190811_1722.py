# Generated by Django 2.2.4 on 2019-08-11 07:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('govtrack', '0011_auto_20190803_2120'),
    ]

    operations = [
        migrations.RenameField('Declaration','date_declared','event_date'),
        migrations.AlterField(
            model_name='declaration',
            name='event_date',
            field=models.DateField(verbose_name='Event date'),
        ),
        migrations.AlterField(
            model_name='declaration',
            name='status',
            field=models.CharField(choices=[('D', 'Declared'), ('N', 'Inactive'), ('R', 'Rejected'), ('V', 'Revoked'), ('P', 'In Progress'), ('L', 'Listing Accepted'), ('J', 'Listing Rejected')], default='D', max_length=1),
        ),
    ]
