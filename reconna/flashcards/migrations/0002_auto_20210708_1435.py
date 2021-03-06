# Generated by Django 2.2.6 on 2021-07-08 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyland',
            name='agent',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bul_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='investmoney',
            name='agent',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invest_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='investmoney',
            name='assign_agent',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
