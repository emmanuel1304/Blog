# Generated by Django 4.1.7 on 2023-03-07 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]
