# Generated by Django 4.2 on 2024-04-02 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0020_ambulance'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='var',
            field=models.TextField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='contact',
            name='var2',
            field=models.TextField(null='True'),
            preserve_default='True',
        ),
    ]
