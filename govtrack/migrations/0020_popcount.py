# Generated by Django 2.2.4 on 2019-08-18 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('govtrack', '0019_declaration_key_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('population', models.PositiveIntegerField()),
                ('date', models.DateField(verbose_name='Declaration date')),
                ('status', models.CharField(choices=[('D', 'Declared'), ('N', 'Inactive'), ('R', 'Rejected'), ('V', 'Revoked'), ('P', 'In Progress'), ('J', 'Listing Rejected')], default='D', max_length=1)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='govtrack.Country')),
                ('declaration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='govtrack.Declaration')),
            ],
        ),
    ]
