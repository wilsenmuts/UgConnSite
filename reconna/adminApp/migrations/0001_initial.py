# Generated by Django 2.2.6 on 2021-07-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('logo', models.ImageField(upload_to='partners')),
                ('notes', models.TextField(blank=True)),
                ('timer', models.DateTimeField()),
            ],
        ),
    ]