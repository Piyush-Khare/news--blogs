# Generated by Django 3.2.6 on 2021-09-04 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogmodel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogmodel',
            old_name='user',
            new_name='email',
        ),
    ]