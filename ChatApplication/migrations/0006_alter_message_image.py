# Generated by Django 3.2.9 on 2021-11-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApplication', '0005_alter_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images/uploads'),
        ),
    ]