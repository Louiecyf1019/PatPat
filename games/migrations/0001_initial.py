# Generated by Django 3.1.7 on 2021-03-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gameinfo',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=500)),
                ('comment_num', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('icon', models.ImageField(upload_to='')),
                ('rating', models.FloatField()),
            ],
        ),
    ]
