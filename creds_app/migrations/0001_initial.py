# Generated by Django 3.1.5 on 2021-01-27 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creds_app.url')),
            ],
        ),
    ]