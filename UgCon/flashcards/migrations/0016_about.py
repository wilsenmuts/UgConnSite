# Generated by Django 2.2.6 on 2020-08-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0015_article_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('describe', models.TextField(blank=True)),
            ],
        ),
    ]
