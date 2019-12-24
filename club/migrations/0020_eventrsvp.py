# Generated by Django 3.0.1 on 2019-12-24 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club', '0019_schoolyear'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRSVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, help_text='(optional) A condition for RSVPing', max_length=200, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rsvps', to='club.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rsvps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
