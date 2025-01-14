# Generated by Django 3.1.7 on 2021-03-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('comment_content', models.CharField(max_length=500)),
                ('comment_date', models.DateTimeField()),
                ('rating', models.FloatField(null=True)),
            ],
        ),
    ]
