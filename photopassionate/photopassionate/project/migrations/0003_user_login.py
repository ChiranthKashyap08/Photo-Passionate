# Generated by Django 4.1.3 on 2022-12-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_add_lens'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
