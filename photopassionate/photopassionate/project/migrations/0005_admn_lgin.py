# Generated by Django 4.1.3 on 2022-12-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_admin_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='admn_lgin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
