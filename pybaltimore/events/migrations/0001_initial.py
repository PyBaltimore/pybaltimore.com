# Generated by Django 2.0.7 on 2018-07-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocalEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('date', models.DateField()),
                ('datetime', models.DateTimeField(blank=True)),
                ('hidden', models.BooleanField()),
                ('location', models.TextField(blank=True)),
            ],
        ),
    ]
