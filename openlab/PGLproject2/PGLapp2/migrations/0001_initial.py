# Generated by Django 3.0.3 on 2020-07-13 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Openlablist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=128)),
                ('phone', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'openlab',
            },
        ),
    ]