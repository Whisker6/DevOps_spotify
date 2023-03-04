# Generated by Django 3.2.2 on 2023-02-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('title', models.CharField(default='', max_length=70)),
                ('song_length', models.CharField(blank=True, default='', max_length=200)),
                ('albumid', models.IntegerField(null=True)),
                ('songid', models.IntegerField(default='', primary_key=True, serialize=False)),
                ('artist', models.CharField(default='', max_length=50)),
            ],
        ),
    ]