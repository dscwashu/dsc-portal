# Generated by Django 3.0.2 on 2020-01-15 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0035_auto_20200111_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAgendaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The public title of the AgendaItem', max_length=200)),
                ('description', models.TextField(blank=True, help_text='The private description that only Core Team members would see. This is where planning details go.', max_length=2000, null=True)),
                ('estimated_start_time', models.TimeField(help_text='The estimated start time of the item. (Within the bounds of the event)')),
                ('estimated_duration', models.DurationField(help_text='How long the item is expected to take.')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='club.Event')),
            ],
            options={
                'ordering': ['estimated_start_time', 'title'],
            },
        ),
    ]
