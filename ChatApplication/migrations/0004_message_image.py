# Generated by Django 3.2.9 on 2021-11-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApplication', '0003_room_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
