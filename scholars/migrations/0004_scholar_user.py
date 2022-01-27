# Generated by Django 4.0.1 on 2022-01-18 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scholars', '0003_alter_scholar_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholar',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]