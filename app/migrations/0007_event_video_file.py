# Generated by Django 5.0.2 on 2024-05-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_newtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='video_file',
            field=models.FileField(default='', upload_to='videos/'),
            preserve_default=False,
        ),
    ]
