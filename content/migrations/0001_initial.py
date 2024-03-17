# Generated by Django 4.2 on 2024-03-17 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('audio_file', models.FileField(upload_to='episode_audio/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
