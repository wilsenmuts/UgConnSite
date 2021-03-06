# Generated by Django 2.2.6 on 2021-07-08 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcards', '0002_auto_20210708_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildhouse',
            name='assign_agent',
        ),
        migrations.RemoveField(
            model_name='buyhouse',
            name='assign_agent',
        ),
        migrations.RemoveField(
            model_name='buyitem',
            name='assign_agent',
        ),
        migrations.RemoveField(
            model_name='buyland',
            name='assign_agent',
        ),
        migrations.RemoveField(
            model_name='donatemoney',
            name='assign_agent',
        ),
        migrations.RemoveField(
            model_name='feesandbills',
            name='assign_agent',
        ),
        migrations.RemoveField(
            model_name='investmoney',
            name='assign_agent',
        ),
        migrations.RemoveField(
            model_name='others',
            name='assign_agent',
        ),
        migrations.AddField(
            model_name='buildhouse',
            name='agent',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='builh_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buyhouse',
            name='agent',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyh_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buyitem',
            name='agent',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equip_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='donatemoney',
            name='agent',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donate_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feesandbills',
            name='agent',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pay_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='others',
            name='agent',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='other_agent', to=settings.AUTH_USER_MODEL),
        ),
    ]
