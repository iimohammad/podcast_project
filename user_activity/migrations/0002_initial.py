# Generated by Django 4.2 on 2024-03-17 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0002_initial'),
        ('user_activity', '0001_initial'),
        ('user_panel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.episode'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followedchannel',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_panel.channel'),
        ),
        migrations.AddField(
            model_name='followedchannel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.episode'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]