# Generated by Django 4.1.3 on 2022-12-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_lens',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=20)),
                ('lenstype', models.CharField(max_length=30)),
                ('mount', models.CharField(max_length=20)),
                ('maxflength', models.CharField(max_length=20)),
                ('minflength', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
