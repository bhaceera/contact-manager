# Generated by Django 2.1.4 on 2018-12-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_remove_contact_contact_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField(max_length=200)),
                ('sex', models.CharField(max_length=10)),
                ('sbu', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
