# Generated by Django 4.1.7 on 2023-02-20 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='text',
        ),
    ]