# Generated by Django 4.0.6 on 2022-09-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_rename_username_contact_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='pno',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='query',
        ),
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10, null='True'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50, null='True'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]