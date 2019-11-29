# Generated by Django 2.2.6 on 2019-11-29 04:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club', '0010_update_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Online', help_text='Where the event is being held.', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='update',
            name='image_url',
            field=models.URLField(blank=True, help_text='Optional url of cover image to display on top of update and on index page.', null=True),
        ),
        migrations.CreateModel(
            name='UpdateComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(help_text='The text of the comment.', max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('update', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.Update')),
            ],
        ),
    ]