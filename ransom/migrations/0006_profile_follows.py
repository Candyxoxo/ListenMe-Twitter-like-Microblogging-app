# Generated by Django 4.1.5 on 2023-04-01 20:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ransom', '0005_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(related_name='followed_profiles', to=settings.AUTH_USER_MODEL),
        ),
    ]