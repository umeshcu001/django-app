# Generated by Django 3.2 on 2021-05-29 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_enquiry_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='username',
            new_name='name',
        ),
    ]
