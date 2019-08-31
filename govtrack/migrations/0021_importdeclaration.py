# Generated by Django 2.2.4 on 2019-08-28 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('govtrack', '0020_popcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportDeclaration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('num_govs', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('area', models.TextField(blank=True, null=True)),
                ('population', models.PositiveIntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('due', models.TextField(blank=True, null=True)),
                ('contact', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='govtrack.Country')),
            ],
        ),
    ]
