# Generated by Django 3.2.3 on 2021-06-01 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='imgc',
            field=models.FileField(upload_to='blog/images'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='lastimg',
            field=models.FileField(upload_to='blog/images'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='mainimg',
            field=models.FileField(upload_to='blog/images'),
        ),
    ]
