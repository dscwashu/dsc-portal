# Generated by Django 3.0.2 on 2020-01-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0026_event_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text='Long descriptionf of the event. Supports Markdown.', max_length=10000),
        ),
    ]
